import * as admin from 'firebase-admin';
import { onDocumentCreated } from 'firebase-functions/v2/firestore';
import { onSchedule } from 'firebase-functions/v2/scheduler';
import { onCall, HttpsError } from 'firebase-functions/v2/https';
import * as logger from 'firebase-functions/logger';

admin.initializeApp();
const db = admin.firestore();

// ============================
// AI 분석 (임시: 간단한 규칙 기반)
// ============================
function simpleAISummary(data: {
  water_liter?: number;
  exercise_freq?: string;
  vitamin_miss?: string;
}): string {
  const msgs: string[] = [];

  if ((data.water_liter ?? 0) < 1.5) {
    msgs.push('물 섭취량이 평균보다 적습니다. 하루 1.5~2L를 목표로 시도해보세요!');
  }
  if (data.exercise_freq === '0회') {
    msgs.push('운동을 거의 하지 않네요! 가벼운 산책부터 시작해보는 것을 추천드려요.');
  }
  if (data.vitamin_miss && data.vitamin_miss !== '0회') {
    msgs.push('영양제 복용이 자주 누락됩니다. 알림 기능을 활용해보는 건 어떨까요?');
  }

  if (msgs.length === 0) {
    return '전체적으로 좋은 루틴을 유지하고 있어요! 지금 페이스를 유지해보세요 🙌';
  }

  return msgs.join(' ');
}


// ======================================
// 1) 설문 저장 시 AI 자동 분석 후 기록
//    경로: users/{uid}/survey/{surveyId}
// ======================================
export const onSurveySubmit = onDocumentCreated(
  'users/{uid}/survey/{surveyId}',
  async (event) => {
    const snap = event.data;
    const uid = event.params.uid as string;

    if (!snap) {
      logger.warn('onSurveySubmit: snapshot is null');
      return;
    }

    const data = snap.data() as {
      water_liter?: number;
      exercise_freq?: string;
      vitamin_miss?: string;
    };

    const aiMessage = simpleAISummary(data);

    await db
      .collection('users')
      .doc(uid)
      .collection('ai_recommendations')
      .add({
        type: 'survey_analysis',
        ai_message: aiMessage,
        timestamp: admin.firestore.FieldValue.serverTimestamp(),
      });

    logger.info('AI recommendation created from survey', { uid });
  }
);


// ======================================
// 2) 매일 아침 8시 능동형 AI 알림 (FCM)
//   - 토큰 위치 변경된 것 반영됨!!
// ======================================
export const morningRoutineReminder = onSchedule(
  {
    schedule: '0 8 * * *',
    timeZone: 'Asia/Seoul',
  },
  async () => {
    // ⬇⬇ 여기 변경됨 (핵심)
    const tokenSnap = await db.collection('notification_tokens').get();

    const tokens: string[] = [];
    tokenSnap.forEach((doc) => {
      const data = doc.data() as { token?: string };
      if (data.token) tokens.push(data.token);
    });

    if (tokens.length === 0) {
      logger.warn('🚨 No notification tokens found');
      return;
    }

    // 멀티 전송 방식
    await admin.messaging().sendEachForMulticast({
      tokens,
      notification: {
        title: '오늘의 건강 루틴 체크 🔔',
        body: '오늘 물, 운동, 영양제 루틴을 시작할 시간이에요! 💪🔥',
      },
    });

    logger.info(`FCM sent to ${tokens.length} devices`);
  }
);


// ======================================
// 3) 일일 기록 점수 분석 API
// ======================================
export const analyzeDailyLog = onCall(
  { region: 'asia-northeast3' },
  async (request) => {
    const auth = request.auth;
    if (!auth) {
      throw new HttpsError('unauthenticated', '로그인이 필요합니다.');
    }

    const { water, exercise, vitamin } = request.data as {
      water: number;
      exercise: number;
      vitamin: boolean;
    };

    let score = 0;
    if (water >= 1.5) score += 30;
    if (exercise >= 30) score += 40;
    if (vitamin) score += 30;

    const uid = auth.uid;
    const todayId = new Date().toISOString().split('T')[0];

    await db
      .collection('users')
      .doc(uid)
      .collection('daily_logs')
      .doc(todayId)
      .set({
        water_today: water,
        exercise_today: exercise,
        vitamin_today: vitamin,
        score,
        timestamp: admin.firestore.FieldValue.serverTimestamp(),
      });

    logger.info('daily log analyzed', { uid, score });

    return { score };
  }
);
