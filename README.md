✨ HOWLIFE – 습관 기반 AI 헬스 코치

당신의 물·운동·영양제 루틴을 꾸준히 유지하도록 돕는
개인 맞춤형 AI 루틴 코치 서비스입니다.

🌱 핵심 기능
📌 사용자 분석 기반 맞춤 제공

설문 기반 사용자 분석

맞춤형 AI 루틴 코멘트 제공

📌 일상 루틴 자동 기록

물 마신 기록

영양제 복용 기록

운동 수행 시간 기록

🧠 AI 기반 피드백

루틴 점수 계산

AI 메시지 생성 및 제공

🧾 기록 데이터 관리

Firebase Firestore 사용

사용자별 루틴 저장

🖥 Web UI 제공

Streamlit 기반

단일 페이지 스크롤형 UI

UI 구성(홈/기록/AI챗/커뮤니티/설정)

🚀 실행 방법

아래 명령어를 그대로 사용하면 됩니다.

1) 프로젝트 클론
git clone https://github.com/gm-15/HowLife.git
cd HowLife

2) Python 가상환경 생성 및 적용
Windows
python -m venv .venv
.venv\Scripts\activate

macOS/Linux
python3 -m venv .venv
source .venv/bin/activate

3) 패키지 설치
pip install -r requirements.txt

4) 실행
streamlit run Howlife-FrontEnd-main/app.py

📦 폴더 구조
HowLife/
├── functions/                       # Firebase Cloud Functions
├── Howlife-FrontEnd-main/
│   ├── app.py                       # Streamlit Main Entry
│   ├── sections/                    # Page sections
│   ├── components/                  # UI widgets
│   ├── firebase_client.py           # Firebase Connection
│   └── data/                        # Mock Data & Static Resources
├── firebase.json
├── firestore.rules
├── firestore.indexes.json
└── README.md

🔥 기술 스택
분야	사용 기술
Frontend	Streamlit, Python
Backend	Firebase Functions (TS), Firestore
Authentication	Firebase Auth
Deployment	Local Dev Mode
DB 구조	사용자 단위 컬렉션 기반 저장
👨‍💻 개발 기여 요소 설명 (발표용 핵심 포인트)

✔ 설문 사용자 데이터 기반 모델링
✔ Firebase Firestore 데이터 연동
✔ Cloud Functions 기반 분석 API 구현
✔ 능동형 알림 설계를 통한 확장 기반 확보
✔ Streamlit UI 구성·상태 관리

발표에서 다음 포인트를 강조해라:

“단순 데이터 저장이 아니라, 사용자 행동 분석 후 AI 피드백 및 루틴 생성까지 제공한다.”

그리고:

“설문 분석 결과를 기반으로 기능 목표를 잡았고 능동적 기능은 FCM 지원 기반으로 확장 설계했다”

⚠️ 사용 시 주의

GitHub 보안을 위해 다음은 제외함:

❌ Firebase Private Key
❌ Service Account Credentials

실제 사용 시 반드시:

👉 Firebase Console에서
👉 Web App 생성 후
👉 API Key로 재셋팅 필요함

해당 위치:

📁 Howlife-FrontEnd-main/firebase_client.py
