"""
기록 섹션 (Firebase 연동 버전)
"""
import streamlit as st
import random
from datetime import datetime
from components.widgets import show_toast, exercise_timer_ui, progress_bar
from data.mock_data import USER_DATA, SUPPLEMENTS, EXERCISE_ROUTINES
from firebase_client import db
import uuid


# ==========================
# 유저 식별 (임시 ID)
# ==========================
def get_user_id():
    """
    로그인 대신 session 기반 유저 UUID 생성
    """
    if "user_id" not in st.session_state:
        st.session_state["user_id"] = str(uuid.uuid4())
    return st.session_state["user_id"]


# ==========================
# Firestore 저장 함수
# ==========================
def save_daily_record(field_name: str, value):
    """
    field_name: water, supplement, exercise 중 하나
    value: 저장되는 값
    """
    user_id = get_user_id()
    today_key = datetime.now().strftime("%Y-%m-%d")

    doc = db.collection("users").document(user_id).collection("records").document(today_key)

    doc.set(
        {field_name: value, "updated_at": datetime.now().isoformat()},
        merge=True
    )


# ==========================
# Firestore 기록 불러오기
# ==========================
def load_daily_record():
    user_id = get_user_id()
    today_key = datetime.now().strftime("%Y-%m-%d")

    doc = (
        db.collection("users")
        .document(user_id)
        .collection("records")
        .document(today_key)
        .get()
    )

    if doc.exists:
        return doc.to_dict()

    return {}


# ==========================
# 메인 UI 렌더링
# ==========================
def render_record():
    st.markdown('<div id="record" data-section="record"></div>', unsafe_allow_html=True)

    # 🔥 오늘 기록 불러오기
    today_record = load_daily_record()

    # ==========================
    # 초기 세션값 설정
    # ==========================
    st.session_state.setdefault("water_current", today_record.get("water", USER_DATA["water_current"]))
    st.session_state.setdefault("supplements", today_record.get("supplements", SUPPLEMENTS.copy()))
    st.session_state.setdefault("exercise_current", today_record.get("exercise", 0))

    # =========== 물 기록 ===========
    st.markdown("### 💧 물 기록")

    water_current = st.session_state["water_current"]
    water_goal = USER_DATA["water_goal"]
    water_progress = min(water_current / water_goal * 100, 100)

    st.markdown(f"**{water_current}ml / {water_goal}ml**")
    progress_bar(water_progress)

    col1, col2 = st.columns(2)

    # 🔥 한 모금
    with col1:
        if st.button("한 모금 (50ml)", use_container_width=True):
            st.session_state["water_current"] += 50
            save_daily_record("water", st.session_state["water_current"])
            show_toast("좋아요! 물 한 모금 성공! 💧", "💙")
            st.rerun()

    # 🔥 한 컵
    with col2:
        if st.button("한 컵 (200ml)", use_container_width=True):
            st.session_state["water_current"] += 200
            save_daily_record("water", st.session_state["water_current"])
            show_toast("물 한 컵 완료! 오늘도 화이팅 💧", "🔥")
            st.rerun()

    st.markdown("---")

    # =========== 영양제 기록 ===========
    st.markdown("### 💊 영양제 기록")

    supplements = st.session_state["supplements"]
    taken_count = sum(1 for s in supplements if s["taken"])
    supplement_goal = USER_DATA["supplement_goal"]
    supplement_progress = taken_count / supplement_goal * 100

    st.markdown(f"**{taken_count}개 / {supplement_goal}개**")
    progress_bar(supplement_progress)

    for supplement in supplements:
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown(f"**{supplement['name']}** ({supplement['timing']})")

        with col2:
            is_taken = st.checkbox(
                "",
                value=supplement["taken"],
                key=f"supplement_{supplement['id']}",
            )

            if is_taken != supplement["taken"]:
                supplement["taken"] = is_taken
                save_daily_record("supplements", supplements)

                if is_taken:
                    show_toast("영양제 챙겼어요 💊 좋아요!", "✨")
                else:
                    show_toast("내일은 잊지 말아요 💊", "🕑")

                st.rerun()

    st.markdown("---")

    # =========== 운동 기록 ===========
    st.markdown("### 🏃 운동 기록")

    # 🔥 운동 루틴 추천 유지
    today_str = datetime.now().strftime("%Y-%m-%d")
    if "exercise_date" not in st.session_state or st.session_state["exercise_date"] != today_str:
        st.session_state["exercise_date"] = today_str
        st.session_state["current_routine"] = random.choice(EXERCISE_ROUTINES)
        st.session_state["routine_feedback"] = None

    routine = st.session_state["current_routine"]
    st.info(f"🤖 오늘의 루틴 추천!\n\n**{routine['title']}**\n{routine['description']}")

    # 피드백 입력
    if st.session_state.get("routine_feedback") is None:
        col1, col2 = st.columns(2)
        with col1:
            if st.button("👍 좋았어요"):
                st.session_state["routine_feedback"] = "good"
                save_daily_record("routine_feedback", "good")
                show_toast("좋았다니 다행이에요! 내일도 화이팅 💪", "👍")
                st.rerun()
        with col2:
            if st.button("😓 힘들었어요"):
                st.session_state["routine_feedback"] = "hard"
                save_daily_record("routine_feedback", "hard")
                show_toast("힘들지만 멋졌어요 💪 다음은 더 가볍게!", "😓")
                st.rerun()
    else:
        fb = st.session_state["routine_feedback"]
        st.caption(f"오늘 피드백: {'👍' if fb == 'good' else '😓'}")

    # 운동 타이머 UI
    timer_result = exercise_timer_ui()

    total_minutes = int(timer_result["elapsed_seconds"] // 60)

    st.session_state["exercise_current"] = total_minutes
    save_daily_record("exercise", total_minutes)

    exercise_goal = USER_DATA["exercise_goal"]
    exercise_progress = min(total_minutes / exercise_goal * 100, 100)

    st.markdown(f"**{total_minutes}분 / 목표 {exercise_goal}분**")
    progress_bar(exercise_progress)
