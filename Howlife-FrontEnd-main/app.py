"""
HOWLIFE 메인 애플리케이션
Streamlit 기반 스크롤형 웹사이트
"""
import streamlit as st
from components.layout import render_sidebar, scroll_to_section
from sections import home, record, ai_chat, community, settings

# 페이지 설정
st.set_page_config(
    page_title="HOWLIFE - 당신의 꾸준함, AI가 함께 만듭니다",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS 스타일 추가 (스크롤 부드럽게)
st.markdown(
    """
    <style>
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    [data-section], [id] {
        scroll-margin-top: 2rem;
        scroll-behavior: smooth;
    }
    html {
        scroll-behavior: smooth;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar 렌더링
render_sidebar()

# 메인 컨텐츠 영역
st.title("🏠 HOWLIFE")
st.caption("건강한 하루를 함께 만들어가요! 💪")
st.markdown("---")

# 홈 섹션
home_container = st.container()
with home_container:
    home.render_home()
    st.markdown("---")

# 기록 섹션
record_container = st.container()
with record_container:
    record.render_record()
    st.markdown("---")

# AI 채팅 섹션
ai_container = st.container()
with ai_container:
    ai_chat.render_ai_chat()
    st.markdown("---")

# 커뮤니티 섹션
community_container = st.container()
with community_container:
    community.render_community()
    st.markdown("---")

# 설정 섹션
settings_container = st.container()
with settings_container:
    settings.render_settings()

# 하단 여백
st.markdown("")
st.markdown("")
st.markdown("---")
st.caption("© 2024 HOWLIFE. 건강한 하루를 응원합니다! 💪")

