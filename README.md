# ✨ HOWLIFE – 습관 기반 AI 헬스 코치

**당신의 물·운동·영양제 루틴을 꾸준히 유지하도록 돕는 개인 맞춤형 AI 루틴 코치 서비스입니다.**

---

## 🟢 핵심 기능

### 📌 사용자 분석 기반 맞춤 제공
* **설문 기반 사용자 분석**: 초기 설문을 통해 사용자의 건강 상태와 목표를 파악합니다.
* **맞춤형 AI 루틴 코멘트**: 분석 데이터를 바탕으로 개인화된 조언을 제공합니다.

### 📌 일상 루틴 자동 기록
* **물 마신 기록**: 일일 수분 섭취량을 간편하게 트래킹합니다.
* **영양제 복용 기록**: 잊기 쉬운 영양제 섭취 여부를 체크합니다.
* **운동 수행 시간 기록**: 운동 시간을 기록하여 성취도를 관리합니다.

### 🧠 AI 기반 피드백
* **루틴 점수 계산**: 수행한 루틴을 점수화하여 직관적으로 보여줍니다.
* **AI 메시지 생성**: 동기 부여를 위한 맞춤형 피드백 메시지를 생성합니다.

### 🧾 기록 데이터 관리 & Web UI
* **Firebase Firestore**: 사용자별 루틴 데이터를 클라우드에 안전하게 저장합니다.
* **Streamlit UI**: 홈, 기록, AI챗, 커뮤니티, 설정이 통합된 단일 페이지 스크롤형(SPA) 인터페이스를 제공합니다.

---

## 🟠 기술 스택

| 분야 | 사용 기술 |
| --- | --- |
| **Frontend** | Streamlit, Python |
| **Backend** | Firebase Functions (TS), Firestore |
| **Auth** | Firebase Auth |
| **Deployment** | Local Dev Mode |
| **DB** | 사용자 단위 컬렉션 기반 저장 |

---

## 🔵 폴더 구조

```bash
HowLife/
├── functions/                       # Firebase Cloud Functions (Backend Logic)
├── Howlife-FrontEnd-main/
│   ├── app.py                       # Streamlit Main Entry Point
│   ├── sections/                    # Page Sections (UI Components)
│   ├── components/                  # Reusable UI Widgets
│   ├── firebase_client.py           # Firebase Connection Handler
│   └── data/                        # Mock Data & Static Resources
├── firebase.json                    # Firebase Configuration
├── firestore.rules                  # Database Security Rules
├── firestore.indexes.json           # DB Index Settings
└── README.md
```

---

## 🟣 실행 방법

### 1. 프로젝트 클론
```bash
git clone https://github.com/gm-15/HowLife.git
cd HowLife
```

### 2. Python 가상환경 생성 및 적용

**Windows**
```bash
python -m venv .venv
.venv\Scripts\activate
```

**macOS/Linux**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. 패키지 설치
```bash
pip install -r requirements.txt
```

### 4. 실행
```bash
streamlit run Howlife-FrontEnd-main/app.py
```

---

## 🔴 개발 기여 포인트 (Key Highlights)

> ### "단순 데이터 저장이 아니라, 사용자 행동 분석 후 AI 피드백 및 루틴 생성까지 제공합니다."

* **✔ 설문 사용자 데이터 기반 모델링**: 단순 기록을 넘어 사용자 특성에 맞춘 데이터 구조 설계
* **✔ Firebase Firestore 데이터 연동**: 실시간 데이터 동기화 및 안정적인 저장소 구축
* **✔ Cloud Functions 기반 분석 API**: 서버리스 환경에서의 효율적인 데이터 분석 로직 구현
* **✔ 능동형 알림 확장 설계**: 설문 분석 결과를 토대로 목표를 설정하고, 향후 FCM(Firebase Cloud Messaging)을 지원하도록 확장성 확보
* **✔ Streamlit UI 구성 및 상태 관리**: Python만으로 직관적이고 반응성 높은 웹 대시보드 구현

---

## ⚠️ 설정 및 주의사항

GitHub 보안 정책에 따라 **Firebase Private Key** 및 **Service Account Credentials**는 리포지토리에 포함되어 있지 않습니다.

실제 실행을 위해서는 다음 단계가 필요합니다:

1. **Firebase Console** 접속 및 Web App 생성
2. `Howlife-FrontEnd-main/firebase_client.py` 파일을 엽니다.
3. 발급받은 **API Key** 및 **설정 정보**를 해당 파일에 입력하여 재설정해야 정상 작동합니다.
