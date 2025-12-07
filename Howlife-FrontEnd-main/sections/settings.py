"""
설정 섹션
"""
import streamlit as st
from data.mock_data import USER_DATA, SUPPLEMENTS

def render_settings():
    """설정 섹션 렌더링"""
    st.markdown('<div id="settings" data-section="settings"></div>', unsafe_allow_html=True)
    
    # settings 초기화
    if "settings" not in st.session_state:
        st.session_state["settings"] = {
            "nickname": USER_DATA["nickname"],
            "profile_image": None,
            "water": {
                "unit": "ml",
                "notification_frequency": "3시간마다",
            },
            "supplements": SUPPLEMENTS.copy(),
            "exercise": {
                "daily_goal_minutes": 30,
                "weekly_goal_days": 3,
                "notification_frequency": "하루 1회",
            },
            "community_public": True,
        }
    
    settings = st.session_state["settings"]
    
    # 프로필
    st.markdown("### 👤 프로필")
    
    col1, col2 = st.columns([1, 2])
    with col1:
        profile_image = st.file_uploader("프로필 이미지", type=["png", "jpg", "jpeg"], key="profile_upload")
        if profile_image:
            st.image(profile_image, use_container_width=True)
            settings["profile_image"] = profile_image
    
    with col2:
        new_nickname = st.text_input("닉네임", value=settings["nickname"])
        if new_nickname != settings["nickname"]:
            settings["nickname"] = new_nickname
        
        st.markdown("")
        if st.button("🚪 로그아웃 (더미)", use_container_width=True):
            st.info("로그아웃 기능은 준비 중입니다.")
        
        if st.button("🗑️ 데이터 초기화", use_container_width=True):
            if st.checkbox("정말 초기화하시겠습니까?"):
                st.session_state["water_current"] = 0
                st.session_state["supplement_current"] = 0
                st.session_state["exercise_current"] = 0
                st.session_state["exercise_elapsed_seconds"] = 0
                st.session_state["exercise_start_time"] = None
                st.session_state["exercise_is_running"] = False
                for supplement in settings["supplements"]:
                    supplement["taken"] = False
                st.success("데이터가 초기화되었습니다.")
                st.rerun()
    
    st.markdown("---")
    
    # 물 설정
    st.markdown("### 💧 물 설정")
    
    water_unit = st.selectbox(
        "기록 단위",
        ["ml", "L", "컵"],
        index=0 if settings["water"]["unit"] == "ml" else (1 if settings["water"]["unit"] == "L" else 2)
    )
    settings["water"]["unit"] = water_unit
    
    water_notification = st.selectbox(
        "알림 빈도",
        ["1시간마다", "2시간마다", "3시간마다", "알림 끄기"],
        index=2 if settings["water"]["notification_frequency"] == "3시간마다" else 0
    )
    settings["water"]["notification_frequency"] = water_notification
    
    st.markdown("---")
    
    # 영양제 설정
    st.markdown("### 💊 영양제 설정")
    
    st.markdown("#### 영양제 목록")
    supplements = settings["supplements"]
    
    for i, supplement in enumerate(supplements):
        col1, col2, col3, col4 = st.columns([2, 2, 1, 1])
        with col1:
            new_name = st.text_input("이름", value=supplement["name"], key=f"supp_name_{i}")
            supplement["name"] = new_name
        with col2:
            new_timing = st.selectbox(
                "복용 타이밍",
                ["아침", "점심", "저녁", "식후"],
                index=["아침", "점심", "저녁", "식후"].index(supplement["timing"]) if supplement["timing"] in ["아침", "점심", "저녁", "식후"] else 0,
                key=f"supp_timing_{i}"
            )
            supplement["timing"] = new_timing
        with col3:
            st.markdown("")
            st.markdown("")
            if st.button("삭제", key=f"supp_del_{i}"):
                supplements.pop(i)
                st.rerun()
    
    if st.button("➕ 영양제 추가"):
        new_supplement = {
            "id": len(supplements) + 1,
            "name": "새 영양제",
            "taken": False,
            "timing": "아침",
        }
        supplements.append(new_supplement)
        st.rerun()
    
    st.markdown("---")
    
    # 운동 설정
    st.markdown("### 🏃 운동 설정")
    
    daily_goal = st.number_input("하루 목표 시간 (분)", min_value=0, value=settings["exercise"]["daily_goal_minutes"])
    settings["exercise"]["daily_goal_minutes"] = int(daily_goal)
    st.session_state["exercise_goal"] = int(daily_goal)
    
    weekly_goal = st.number_input("주당 목표 운동일", min_value=0, max_value=7, value=settings["exercise"]["weekly_goal_days"])
    settings["exercise"]["weekly_goal_days"] = int(weekly_goal)
    
    exercise_notification = st.selectbox(
        "알림 빈도",
        ["하루 1회", "하루 2회", "알림 끄기"],
        index=0 if settings["exercise"]["notification_frequency"] == "하루 1회" else (1 if settings["exercise"]["notification_frequency"] == "하루 2회" else 2),
        key="exercise_notif"
    )
    settings["exercise"]["notification_frequency"] = exercise_notification
    
    st.markdown("---")
    
    # 커뮤니티 공개 설정
    st.markdown("### 👥 커뮤니티 공개 설정")
    
    community_public = st.checkbox("커뮤니티에 내 활동 공개", value=settings["community_public"])
    settings["community_public"] = community_public
    
    st.markdown("")
    
    # 설정 저장 안내
    st.info("💡 설정은 자동으로 저장됩니다.")


