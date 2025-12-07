"""
재사용 가능한 위젯 컴포넌트
"""
import streamlit as st
import random
from datetime import datetime, timedelta
from typing import Dict, List

def goal_card(title: str, current: float, goal: float, unit: str = "", icon: str = "🎯") -> None:
    """목표 카드 위젯"""
    progress = min(current / goal * 100, 100) if goal > 0 else 0
    
    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown(f"### {icon} {title}")
        st.markdown(f"**{current:.0f}{unit} / {goal:.0f}{unit}**")
    with col2:
        st.metric("진행률", f"{progress:.0f}%")
    
    progress_bar(progress)

def progress_bar(percentage: float, height: int = 20) -> None:
    """진행률 바 위젯"""
    st.progress(percentage / 100)

def weekly_calendar(week_data: List[Dict]) -> None:
    """주간 달력 위젯"""
    st.markdown("### 📅 주간 꾸준함 달력")
    
    cols = st.columns(7)
    today = datetime.now().strftime("%Y-%m-%d")
    
    for idx, day_data in enumerate(week_data):
        with cols[idx]:
            date_obj = datetime.strptime(day_data["date"], "%Y-%m-%d")
            day_name = day_data["day"]
            rate = day_data["completion_rate"]
            
            # 오늘 날짜 강조
            is_today = day_data["date"] == today
            date_display = date_obj.strftime("%m/%d")
            
            if is_today:
                st.markdown(f"**{date_display}**")
                st.markdown(f"**{day_name}**")
            else:
                st.markdown(date_display)
                st.markdown(day_name)
            
            # 달성도에 따른 색상
            if rate >= 80:
                color = "🟢"
            elif rate >= 60:
                color = "🟡"
            else:
                color = "🔴"
            
            st.markdown(f"{color} {rate}%")
            st.progress(rate / 100)

def show_toast(message: str, icon: str = "🎉") -> None:
    """스낵바 응원 메시지"""
    st.toast(f"{icon} {message}")

def exercise_timer_ui() -> Dict:
    """운동 타이머 UI (시작/종료 + 경과 시간 표시)"""
    st.markdown("### ⏱️ 운동 시간 측정")
    
    # session_state 초기화
    if "exercise_start_time" not in st.session_state:
        st.session_state["exercise_start_time"] = None
    if "exercise_elapsed_seconds" not in st.session_state:
        st.session_state["exercise_elapsed_seconds"] = 0
    if "exercise_is_running" not in st.session_state:
        st.session_state["exercise_is_running"] = False
    
    # 현재 경과 시간 계산
    if st.session_state["exercise_is_running"] and st.session_state["exercise_start_time"]:
        elapsed = datetime.now() - st.session_state["exercise_start_time"]
        elapsed_seconds = elapsed.total_seconds()
        current_elapsed = st.session_state["exercise_elapsed_seconds"] + elapsed_seconds
        
        # 실시간 경과 시간 표시
        current_minutes = int(elapsed_seconds // 60)
        current_seconds = int(elapsed_seconds % 60)
        st.info(f"⏱️ **현재 운동 시간: {current_minutes}분 {current_seconds}초** (진행 중...)")
    else:
        current_elapsed = st.session_state["exercise_elapsed_seconds"]
    
    # 누적 시간 표시 (분:초)
    minutes = int(current_elapsed // 60)
    seconds = int(current_elapsed % 60)
    
    # 큰 숫자로 표시
    st.markdown(f"### 누적 시간: {minutes:02d}:{seconds:02d}")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("🏃 운동 시작", use_container_width=True, disabled=st.session_state["exercise_is_running"]):
            st.session_state["exercise_start_time"] = datetime.now()
            st.session_state["exercise_is_running"] = True
            # 운동 시작 응원 메시지
            st.toast("운동 시작! 화이팅! 💪")
            st.rerun()
    
    with col2:
        if st.button("⏹️ 운동 종료", use_container_width=True, disabled=not st.session_state["exercise_is_running"]):
            if st.session_state["exercise_start_time"]:
                elapsed = datetime.now() - st.session_state["exercise_start_time"]
                elapsed_seconds = elapsed.total_seconds()
                st.session_state["exercise_elapsed_seconds"] += elapsed_seconds
                st.session_state["exercise_start_time"] = None
                st.session_state["exercise_is_running"] = False
                
                # 종료 시 응원 메시지
                elapsed_minutes = int(elapsed_seconds // 60)
                total_minutes = int(st.session_state["exercise_elapsed_seconds"] // 60)
                encouragement_messages = [
                    f"+{elapsed_minutes}분 운동 추가! 누적 {total_minutes}분! 멋지다 🔥",
                    "좋아요! 오늘 목표에 한 걸음 더 가까워졌어요! 💪",
                    "멋져요! 꾸준함이 쌓이고 있어요 🔥",
                ]
                st.toast(random.choice(encouragement_messages))
                st.rerun()
    
    return {
        "is_running": st.session_state["exercise_is_running"],
        "elapsed_seconds": st.session_state["exercise_elapsed_seconds"],
        "current_elapsed": current_elapsed,
    }


