"""
AI 채팅 섹션
"""
import streamlit as st
from datetime import datetime

def render_ai_chat():
    """AI 채팅 섹션 렌더링"""
    st.markdown('<div id="ai_chat" data-section="ai_chat"></div>', unsafe_allow_html=True)
    
    # 채팅 히스토리 초기화
    if "chat_history" not in st.session_state:
        st.session_state["chat_history"] = []
        # 섹션 시작 시 능동형 질문 1개 자동 노출
        st.session_state["chat_history"].append({
            "role": "ai",
            "message": "오늘 하루 수고 많았어! 내가 추천한 운동은 어땠어?",
            "timestamp": datetime.now().strftime("%H:%M")
        })
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # 채팅 로그
        st.markdown("### 💬 AI 채팅")
        
        chat_container = st.container()
        with chat_container:
            for chat in st.session_state["chat_history"]:
                if chat["role"] == "user":
                    with st.chat_message("user"):
                        st.write(chat["message"])
                        st.caption(chat.get("timestamp", ""))
                else:
                    with st.chat_message("assistant"):
                        st.write(chat["message"])
                        st.caption(chat.get("timestamp", ""))
    
    with col2:
        # 기능 버튼
        st.markdown("### 🛠️ 기능")
        
        if st.button("📋 루틴 추천", use_container_width=True):
            response = "오늘은 가벼운 스트레칭과 10분 걷기를 추천해요! 꾸준함이 가장 중요하답니다. 💪"
            st.session_state["chat_history"].append({
                "role": "ai",
                "message": response,
                "timestamp": datetime.now().strftime("%H:%M")
            })
            st.rerun()
        
        if st.button("🔍 건강 정보 검색", use_container_width=True):
            response = "물은 하루 2L 이상 마시는 것이 좋아요. 식사 전후에 마시면 소화에도 도움이 됩니다! 💧"
            st.session_state["chat_history"].append({
                "role": "ai",
                "message": response,
                "timestamp": datetime.now().strftime("%H:%M")
            })
            st.rerun()
        
        if st.button("📊 주간 리포트", use_container_width=True):
            response = "이번 주 목표 달성률: 물 85%, 영양제 90%, 운동 60%. 운동 시간을 조금 더 늘려보세요! 📈"
            st.session_state["chat_history"].append({
                "role": "ai",
                "message": response,
                "timestamp": datetime.now().strftime("%H:%M")
            })
            st.rerun()
        
        if st.button("📅 월간 리포트", use_container_width=True):
            response = "이번 달 평균 달성률: 물 88%, 영양제 92%, 운동 65%. 꾸준히 노력하고 계시네요! 🌟"
            st.session_state["chat_history"].append({
                "role": "ai",
                "message": response,
                "timestamp": datetime.now().strftime("%H:%M")
            })
            st.rerun()
        
        if st.button("🔄 루틴 갱신", use_container_width=True):
            response = "새로운 루틴을 추천해드릴게요! 오늘부터 시작해보세요. 화이팅! 🎯"
            st.session_state["chat_history"].append({
                "role": "ai",
                "message": response,
                "timestamp": datetime.now().strftime("%H:%M")
            })
            st.rerun()
    
    # 하단 입력창
    st.markdown("---")
    user_input = st.chat_input("메시지를 입력하세요...")
    
    if user_input:
        # 사용자 메시지 추가
        st.session_state["chat_history"].append({
            "role": "user",
            "message": user_input,
            "timestamp": datetime.now().strftime("%H:%M")
        })
        
        # 더미 AI 자동 응답
        responses = [
            "좋은 질문이에요! 그 부분에 대해 더 자세히 알려드릴게요. 💡",
            "꾸준함이 가장 중요해요. 작은 것부터 시작해보세요! 화이팅! 💪",
            "당신의 노력을 응원해요! 건강한 하루 되세요! 🌟",
            "좋은 습관을 만들고 계시네요! 계속 이렇게 꾸준히 해보세요! ✨",
        ]
        import random
        ai_response = random.choice(responses)
        
        st.session_state["chat_history"].append({
            "role": "ai",
            "message": ai_response,
            "timestamp": datetime.now().strftime("%H:%M")
        })
        
        st.rerun()
    
    st.markdown("")


