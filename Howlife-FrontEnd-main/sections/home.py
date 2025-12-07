"""
홈 섹션
"""
import streamlit as st
import random
from datetime import datetime, timedelta
from components.widgets import goal_card, weekly_calendar, show_toast
from data.mock_data import (
    USER_DATA, 
    YESTERDAY_FEEDBACK, 
    AI_INSIGHTS,
    get_weekly_calendar_data
)

def get_current_insight():
    """1시간마다 갱신되는 AI Insight 반환"""
    now = datetime.now()
    
    # 마지막 갱신 시간 확인
    if "last_insight_time" not in st.session_state:
        st.session_state["last_insight_time"] = now
        st.session_state["current_insight"] = random.choice(AI_INSIGHTS)
        return st.session_state["current_insight"]
    
    # 1시간 경과 확인
    time_diff = now - st.session_state["last_insight_time"]
    if time_diff >= timedelta(hours=1):
        # 새로운 Insight 생성
        st.session_state["last_insight_time"] = now
        st.session_state["current_insight"] = random.choice(AI_INSIGHTS)
    
    return st.session_state.get("current_insight", random.choice(AI_INSIGHTS))

def render_home():
    """홈 섹션 렌더링"""
    st.markdown('<div id="home" data-section="home"></div>', unsafe_allow_html=True)
    
    # (1) AI Insight (1시간마다 자동 갱신)
    st.markdown("### 🤖 AI Insight")
    insight = get_current_insight()
    st.info(f"💡 {insight}")
    st.markdown("")
    
    # (2) 오늘의 목표 및 진행률
    st.markdown("### 📊 오늘의 목표")
    
    # 물 목표
    goal_card(
        "물 섭취",
        st.session_state.get("water_current", USER_DATA["water_current"]),
        st.session_state.get("water_goal", USER_DATA["water_goal"]),
        "ml",
        "💧"
    )
    st.markdown("")
    
    # 영양제 목표
    supplement_current = st.session_state.get("supplement_current", USER_DATA["supplement_current"])
    supplement_goal = st.session_state.get("supplement_goal", USER_DATA["supplement_goal"])
    goal_card(
        "영양제 복용",
        supplement_current,
        supplement_goal,
        "개",
        "💊"
    )
    st.markdown("")
    
    # 운동 목표
    exercise_current = st.session_state.get("exercise_current", USER_DATA["exercise_current"])
    exercise_goal = st.session_state.get("exercise_goal", USER_DATA["exercise_goal"])
    goal_card(
        "운동 시간",
        exercise_current,
        exercise_goal,
        "분",
        "🏃"
    )
    st.markdown("")
    
    # (3) 전날 피드백 + 응원과 격려
    st.markdown("### 💬 어제 피드백 + 응원과 격려")
    st.success(f"✨ {YESTERDAY_FEEDBACK['message']}")
    st.markdown("")
    
    # (4) 주간 꾸준함 달력
    week_data = get_weekly_calendar_data()
    weekly_calendar(week_data)
    st.markdown("")


