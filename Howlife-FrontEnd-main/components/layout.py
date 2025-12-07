"""
레이아웃 컴포넌트 - Sidebar 및 섹션 네비게이션
"""
import streamlit as st

def render_sidebar():
    """Sidebar 렌더링 - 섹션 이동 네비게이션"""
    with st.sidebar:
        st.title("🏠 HOWLIFE")
        st.markdown("---")
        
        # 섹션 네비게이션 - HTML anchor로 직접 이동
        if st.button("🏠 홈", use_container_width=True):
            st.markdown("<script>location.href='#home'</script>", unsafe_allow_html=True)
            st.rerun()
        
        if st.button("📝 기록", use_container_width=True):
            st.markdown("<script>location.href='#record'</script>", unsafe_allow_html=True)
            st.rerun()
        
        if st.button("🤖 AI 채팅", use_container_width=True):
            st.markdown("<script>location.href='#ai_chat'</script>", unsafe_allow_html=True)
            st.rerun()
        
        if st.button("👥 커뮤니티", use_container_width=True):
            st.markdown("<script>location.href='#community'</script>", unsafe_allow_html=True)
            st.rerun()
        
        if st.button("⚙️ 설정", use_container_width=True):
            st.markdown("<script>location.href='#settings'</script>", unsafe_allow_html=True)
            st.rerun()
        
        st.markdown("---")
        st.caption("건강한 하루를 응원합니다! 💪")

def render_section_title(title: str, icon: str = ""):
    """섹션 제목 렌더링"""
    st.markdown("---")
    st.markdown(f"## {icon} {title}")
    st.markdown("")

def scroll_to_section(section_id: str):
    """특정 섹션으로 스크롤 이동 (JavaScript 사용 - 부드러운 슬라이드)"""
    if "scroll_to" in st.session_state and st.session_state["scroll_to"] == section_id:
        # JavaScript로 부드러운 스크롤 이동
        st.markdown(
            f"""
            <script>
                function scrollToSection() {{
                    // ID로 먼저 시도, 없으면 data-section으로
                    let element = document.getElementById('{section_id}');
                    if (!element) {{
                        element = document.querySelector('[data-section="{section_id}"]');
                    }}
                    if (element) {{
                        // 부드러운 스크롤 애니메이션
                        element.scrollIntoView({{
                            behavior: 'smooth',
                            block: 'start',
                            inline: 'nearest'
                        }});
                    }}
                }}
                // DOM이 로드된 후 실행
                if (document.readyState === 'loading') {{
                    document.addEventListener('DOMContentLoaded', scrollToSection);
                }} else {{
                    scrollToSection();
                }}
                // Streamlit 렌더링 지연 대응 (여러 번 시도)
                setTimeout(scrollToSection, 100);
                setTimeout(scrollToSection, 300);
                setTimeout(scrollToSection, 500);
            </script>
            """,
            unsafe_allow_html=True
        )
        # 스크롤 후 상태 초기화
        del st.session_state["scroll_to"]


