"""
커뮤니티 섹션
"""
import streamlit as st
from data.mock_data import COMMUNITY_POSTS, HEALTH_TIPS, AI_RECOMMENDED_POSTS
from datetime import datetime

def render_community():
    """커뮤니티 섹션 렌더링"""
    st.markdown('<div id="community" data-section="community"></div>', unsafe_allow_html=True)
    
    # 좋아요 상태 초기화
    if "likes" not in st.session_state:
        st.session_state["likes"] = {}
        # 초기 좋아요 수 설정
        for post in COMMUNITY_POSTS:
            post_id = post["id"]
            if post_id not in st.session_state["likes"]:
                st.session_state["likes"][post_id] = {"count": 0, "liked": False}
    
    # 탭 구성
    tab1, tab2 = st.tabs(["📱 피드", "💡 경험/정보 공유"])
    
    with tab1:
        st.markdown("### 📱 피드")
        
        # 검색 기능
        search_query = st.text_input("🔍 검색", placeholder="게시글 내용으로 검색...", key="feed_search")
        
        # 글 작성 폼
        with st.expander("✍️ 새 글 작성"):
            post_content = st.text_area("내용을 입력하세요", height=100)
            uploaded_image = st.file_uploader("이미지 업로드", type=["png", "jpg", "jpeg"])
            
            if st.button("게시하기"):
                if post_content:
                    # 더미로 게시물 추가
                    new_post = {
                        "id": len(COMMUNITY_POSTS) + 1,
                        "nickname": st.session_state.get("settings", {}).get("nickname", "홀라이퍼"),
                        "date": datetime.now().strftime("%Y-%m-%d"),
                        "content": post_content,
                        "image": uploaded_image,
                    }
                    COMMUNITY_POSTS.insert(0, new_post)
                    st.success("글이 게시되었습니다! 🎉")
                    st.rerun()
                else:
                    st.warning("내용을 입력해주세요.")
        
        st.markdown("---")
        
        # 검색 필터링 적용
        if search_query:
            filtered_posts = [p for p in COMMUNITY_POSTS if search_query.lower() in p["content"].lower()]
            if not filtered_posts:
                st.info(f"'{search_query}'에 대한 검색 결과가 없습니다.")
        else:
            filtered_posts = COMMUNITY_POSTS
        
        # 피드 게시물 표시
        for post in filtered_posts:
            post_id = post["id"]
            
            # 좋아요 상태 초기화 (새 게시물인 경우)
            if post_id not in st.session_state["likes"]:
                st.session_state["likes"][post_id] = {"count": 0, "liked": False}
            
            with st.container():
                # 헤더 (프로필 + 좋아요 버튼)
                col1, col2, col3 = st.columns([1, 4, 1])
                with col1:
                    st.markdown("👤")  # 프로필 이미지 placeholder
                with col2:
                    st.markdown(f"**{post['nickname']}** · {post['date']}")
                with col3:
                    # 좋아요 버튼
                    like_key = f"like_{post_id}"
                    like_state = st.session_state["likes"][post_id]
                    
                    # 하트 색상 결정
                    heart_emoji = "❤️" if like_state["liked"] else "🤍"
                    like_count = like_state["count"]
                    
                    if st.button(f"{heart_emoji} {like_count}", key=like_key, use_container_width=True):
                        # 토글 기능
                        if like_state["liked"]:
                            # 좋아요 취소
                            like_state["liked"] = False
                            like_state["count"] = max(0, like_state["count"] - 1)
                        else:
                            # 좋아요 추가
                            like_state["liked"] = True
                            like_state["count"] += 1
                        st.rerun()
                
                st.markdown(post['content'])
                
                if post.get('image'):
                    st.image(post['image'], use_container_width=True)
                
                st.markdown("---")
    
    with tab2:
        st.markdown("### 💡 경험/정보 공유")
        
        # 검색 기능
        search_query_info = st.text_input("🔍 검색", placeholder="제목이나 내용으로 검색...", key="info_search")
        
        # 건강 팁 카드 리스트
        st.markdown("#### 📚 건강 팁")
        
        # 검색 필터링 적용
        if search_query_info:
            filtered_tips = [t for t in HEALTH_TIPS if search_query_info.lower() in t["title"].lower() or search_query_info.lower() in t["content"].lower()]
            if not filtered_tips:
                st.info(f"'{search_query_info}'에 대한 검색 결과가 없습니다.")
            else:
                for tip in filtered_tips:
                    with st.expander(f"💡 {tip['title']}"):
                        st.markdown(tip['content'])
        else:
            for tip in HEALTH_TIPS:
                with st.expander(f"💡 {tip['title']}"):
                    st.markdown(tip['content'])
        
        st.markdown("---")
        
        # AI 추천 글
        st.markdown("#### 🤖 AI 추천 글")
        
        # 검색 필터링 적용
        if search_query_info:
            filtered_ai_posts = [p for p in AI_RECOMMENDED_POSTS if search_query_info.lower() in p["title"].lower() or search_query_info.lower() in p["content"].lower()]
            if not filtered_ai_posts:
                st.info(f"'{search_query_info}'에 대한 검색 결과가 없습니다.")
            else:
                for ai_post in filtered_ai_posts:
                    with st.container():
                        st.info(f"**{ai_post['title']}**\n\n{ai_post['content']}")
                        st.markdown("")
        else:
            for ai_post in AI_RECOMMENDED_POSTS:
                with st.container():
                    st.info(f"**{ai_post['title']}**\n\n{ai_post['content']}")
                    st.markdown("")
    
    st.markdown("")


