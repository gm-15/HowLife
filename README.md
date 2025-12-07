📌 README.md 최종본

아래 내용 그대로 README.md 생성하자.

🏠 HOWLIFE 서비스

"꾸준함을 설계하는 자기관리 플랫폼"

AI 기반 분석 + 지속적 행동 유도 UI + Firebase 반영 기반 개인화 시스템

🌟 핵심 기능
1️⃣ 물 섭취 관리

한 모금 / 한 컵 기록

progress bar 실시간 반영

목표 대비 비율 표시

2️⃣ 영양제 복용 관리

영양제별 상태 관리

복용 완료 시 encouraging toast

3️⃣ 운동시간 측정

타이머 기반 기록

logging 저장

daily_rewards까지 확장 가능 구조

🔥 능동형 AI 기능
AI inference 규칙
물 섭취 부족 → 1.5L 이상 유도 메시지
운동 기록 부족 → 가벼운 루틴 제안
영양제 미흡 → 행동 reinforcement


Firebase Function에서 생성되는 Output:

{
  "ai_message": "...",
  "timestamp": "..."
}

🛠 기술 스택
Layer	Tech
Front	Python Streamlit
DB	Firebase Firestore
Backend	Firebase Cloud Functions
Messaging	Firebase Cloud Messaging
AI	Rule-based AI
📂 DB 구조
users/{uid}/daily_logs/{date}
users/{uid}/ai_recommendations/{autoId}
notification_tokens/{id}

🚀 실행 방법
pip install -r requirements.txt
streamlit run app.py

🧪 테스트 방법

UI 동작 실행

Firestore → Data에서 정보 반영 확인

Cloud Functions 로그 확인

📌 개발자 Note

본 프로젝트는
HCI 관점에서 반복 행동을 설계하고
AI 기반 피드백을 통해 사용자 지속성을 강화하는 것을 목표로 제작되었음.