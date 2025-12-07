🌱 HOWLIFE – 습관 기반 AI 헬스 코치

건강 루틴(물‧운동‧영양제)을 꾸준히 유지하도록 돕는 개인 맞춤형 AI 루틴 코치 서비스입니다.

설문 기반 사용자 분석

루틴 자동 기록

하루 루틴 점수화

기본적인 건강 피드백 제공

백엔드 Firebase 기반 구현

Streamlit 기반 Web UI 제공

🚀 실행 방법
1) 프로젝트 클론
git clone https://github.com/gm-15/HowLife.git
cd HowLife

2) Python 가상환경 구성
python -m venv .venv
source .venv/Scripts/activate  # Windows

3) Streamlit 패키지 설치
pip install -r requirements.txt

🔐 Firebase Key 설정 (필수)

보안을 위해 키는 GitHub에 포함되어 있지 않습니다.

아래 파일을 직접 생성해야 합니다 👇

.streamlit/secrets.toml


📌 아래 내용을 직접 입력하세요:

[firebase]
PROJECT_ID="howlife-hci"
PRIVATE_KEY="-----BEGIN PRIVATE KEY-----...-----END PRIVATE KEY-----"
CLIENT_EMAIL="firebase-adminsdk-????@howlife-hci.iam.gserviceaccount.com"


주의

PRIVATE_KEY 줄바꿈(엔터)은 반드시 모두 \n 로 변경해야 합니다
예시)

-----BEGIN PRIVATE KEY-----
abcde....
-----END PRIVATE KEY-----


⇒ 아래처럼 넣어야 함

"-----BEGIN PRIVATE KEY-----\nabcde...\n-----END PRIVATE KEY-----\n"

▶ 앱 실행
streamlit run app.py


실행 후 자동으로 브라우저 실행됨
👉 http://localhost:8501

🏗 프로젝트 구조
HowLife/
│ app.py                  # 메인 UI
│ requirements.txt
│ firebase_client.py      # Firebase 연결 모듈
│ .streamlit/
│   └─ secrets.toml       # 개인 키 저장
│ functions/              # Firebase Cloud Functions
│ sections/
│   ├─ home.py
│   ├─ record.py
│   ├─ ai_chat.py
│   ├─ community.py
│   └─ settings.py
│ components/
│   ├─ widgets.py
│   └─ layout.py

🧠 현재 제공 기능
🌟 Record Page

✔ 물 섭취 기록
✔ 영양제 체크 기록
✔ 운동 기록 & 타이머
✔ 진행률 계산 및 응원 메시지 출력

🌟 AI Feedback 기능

✔ survey 저장 시 자동 추천 메시지 생성
✔ daily log score 계산 API 제공

Firebase Functions 기반

🌟 사용자 설정

목표량 변경

영양제 추가/삭제

알림 빈도 설정 UI 제공
(실제 Push 알림은 배포 시 적용됨)

🔥 능동형 기능 (개발 완료)

아래 기능이 server-side에서 작동함

① 설문 저장 → AI 분석 자동 실행

저장 경로:

users/{uid}/survey/{surveyId}


결과 저장 위치:

users/{uid}/ai_recommendations/

② 매일 오전 8시 알림 예약

(만약 Firebase Blaze 요금제 가입 시 🔔 Push 가능)

오늘 물, 운동, 영양제 루틴을 시작해볼까요?

③ 하루 기록 → 점수화 및 저장

프론트에서 호출 함수:

analyzeDailyLog()


저장 경로:

users/{uid}/daily_logs/{YYYY-MM-DD}

💡 Future Dev Roadmap
항목	상태
실시간 PUSH 알림	서버 완료, 프론트 브라우저 토큰 연동 필요
AI 추천 루틴 고도화	예정
맞춤형 분석 리포트	예정
운동추천 기반 난이도 조절	예정
커뮤니티 기능 확장(진척도 공유)	예정
🔒 GitHub Push Protection 관련 안내

이 프로젝트는 아래 규칙을 준수해야 함

❌ Key 포함 금지
❌ firebase-key.json 저장 금지
❌ secrets.toml commit 금지

📌 .gitignore에 포함됨

firebase-key.json
*.json
.streamlit/secrets.toml

🙌 팀 기여도 정리
역할	담당
Front-end	UI/UX • 화면 구성 • Streamlit
Back-end	Firebase 설계 • 데이터 구조 • Functions • 인증
AI logic	Survey 분석 규칙 설계 • 점수 계산 공식
🍀 발표 핵심 메시지

HOWLIFE는 다음을 돕는 서비스입니다.

“사용자가 원래 하고 싶던 건강 루틴을 AI가 능동적 피드백으로 유지할 수 있도록 설계된 서비스”

핵심 키워드:

✔ 사용자 설문 기반 개인화
✔ 능동적 메시지 기반 행동 유지
✔ UI 상에 루틴 변화를 시각화
✔ 행동 과학 기반 반복 유지
