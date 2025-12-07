"""
더미 데이터 모듈
"""
from datetime import datetime, timedelta
from typing import List, Dict

# 유저 더미 데이터
USER_DATA = {
    "nickname": "홀라이퍼",
    "profile_image": None,
    "water_goal": 2000,  # ml
    "water_current": 800,
    "supplement_goal": 3,
    "supplement_current": 1,
    "exercise_goal": 30,  # minutes
    "exercise_current": 0,
}

# 영양제 더미 리스트
SUPPLEMENTS = [
    {"id": 1, "name": "비타민D", "taken": False, "timing": "아침"},
    {"id": 2, "name": "오메가3", "taken": False, "timing": "점심"},
    {"id": 3, "name": "마그네슘", "taken": False, "timing": "저녁"},
]

# 커뮤니티 글 더미
COMMUNITY_POSTS = [
    {
        "id": 1,
        "nickname": "건강러버",
        "date": "2024-01-15",
        "content": "오늘 물 2L 마셨어요! 목표 달성! 💪",
        "image": None,
    },
    {
        "id": 2,
        "nickname": "운동맨",
        "date": "2024-01-15",
        "content": "30분 조깅 완료! 하루하루가 성장이에요 🏃",
        "image": None,
    },
    {
        "id": 3,
        "nickname": "영양제러버",
        "date": "2024-01-14",
        "content": "비타민D 복용 시작한 지 1주일, 컨디션이 좋아졌어요!",
        "image": None,
    },
]

# 건강 팁 더미
HEALTH_TIPS = [
    {
        "title": "물 마시는 습관 만들기",
        "content": "아침에 일어나자마자 물 한 잔, 식사 전후 물 한 잔씩 마시면 하루 목표를 쉽게 달성할 수 있어요!",
    },
    {
        "title": "운동 전후 영양 섭취",
        "content": "운동 전에는 탄수화물, 운동 후에는 단백질을 섭취하면 효과적입니다.",
    },
    {
        "title": "영양제 복용 타이밍",
        "content": "지용성 비타민(비타민D, E)은 식사와 함께, 수용성 비타민은 공복에 복용하는 것이 좋아요.",
    },
]

# AI 추천 글 더미
AI_RECOMMENDED_POSTS = [
    {
        "title": "당신의 건강 패턴 분석 결과",
        "content": "지난 주 데이터를 분석한 결과, 물 섭취는 꾸준하지만 운동 빈도가 조금 부족해요. 주 3회 이상 운동을 하면 더 좋은 결과를 얻을 수 있을 거예요!",
    },
    {
        "title": "이번 주 목표 달성률",
        "content": "물 섭취: 85%, 영양제: 90%, 운동: 60%. 운동 시간을 조금 더 늘려보세요!",
    },
]

# 주간 달력 더미 데이터
def get_weekly_calendar_data() -> List[Dict]:
    """주간 달력 데이터 생성"""
    today = datetime.now()
    week_data = []
    
    for i in range(7):
        date = today - timedelta(days=6-i)
        # 랜덤한 달성도 (더미)
        completion_rate = 60 + (i * 5)  # 60% ~ 90%
        week_data.append({
            "date": date.strftime("%Y-%m-%d"),
            "day": date.strftime("%a"),
            "completion_rate": min(completion_rate, 100),
        })
    
    return week_data

# 전날 피드백 더미
YESTERDAY_FEEDBACK = {
    "message": "어제 운동이 조금 부족했어요. 그래도 꾸준한 점이 멋져요!",
    "water_rate": 90,
    "supplement_rate": 100,
    "exercise_rate": 50,
}

# AI Insight 더미 (다양한 문구 리스트)
AI_INSIGHTS = [
    "물 마신 지 3시간 지났어요! 한 잔 어때요?",
    "오늘 아직 영양제를 1개만 복용하셨네요. 점심 시간에 오메가3를 챙겨보세요!",
    "운동 시간이 부족해요. 지금 10분만 걸어도 목표에 한 걸음 더 가까워져요!",
    "오늘 하루도 수고 많으셨어요! 물 한 잔으로 하루를 마무리해볼까요? 💧",
    "영양제 복용 시간이에요! 건강한 습관을 만들어가고 계시네요! 💊",
    "오후 시간, 가벼운 스트레칭 어떠세요? 몸이 좋아할 거예요! 🧘",
    "목표의 절반을 달성하셨어요! 계속 화이팅! 💪",
    "규칙적인 생활 패턴이 건강의 열쇠예요. 지금까지 잘하고 계세요! ✨",
    "물 섭취가 충분하시네요! 수분 보충을 잘 하고 계세요! 💧",
    "운동 습관이 자리잡고 있어요! 작은 실천이 큰 변화를 만듭니다! 🏃",
    "영양제를 꾸준히 복용하고 계시네요! 건강 관리의 기본이에요! 💊",
    "오늘도 목표를 향해 한 걸음씩 나아가고 계세요! 응원합니다! 🌟",
]

# 운동 루틴 추천 더미
EXERCISE_ROUTINES = [
    {
        "title": "오늘은 20분 러닝 + 10분 스트레칭 추천할게!",
        "description": "가벼운 조깅으로 시작하고 마무리는 스트레칭으로 몸을 풀어주세요.",
    },
    {
        "title": "15분 홈트레이닝 + 5분 스트레칭 어떠세요?",
        "description": "집에서 할 수 있는 간단한 운동으로 시작해보세요!",
    },
    {
        "title": "30분 걷기 + 10분 근력운동 추천해요!",
        "description": "산책하며 몸을 움직이고, 간단한 근력운동으로 마무리하세요.",
    },
    {
        "title": "20분 요가 + 10분 명상으로 하루를 시작해볼까요?",
        "description": "마음을 차분히 하고 몸을 부드럽게 움직여보세요.",
    },
    {
        "title": "25분 사이클링 + 5분 쿨다운 추천합니다!",
        "description": "유산소 운동으로 심폐지구력을 기르고 쿨다운으로 마무리하세요.",
    },
]


