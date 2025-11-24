import streamlit as st

# 배경 이미지 및 스타일을 설정하는 함수
def set_background_image_strict():
    # Streamlit의 메인 컨테이너에 CSS를 적용하여 배경 이미지를 강제 지정합니다.
    css = """
    <style>
    /* Streamlit 전체 앱 컨테이너 */
    .stApp {
        background-color: #f0f2f6; /* 배경 이미지가 로드되지 않을 때 대비 */
    }

    /* 배경 이미지 레이어를 생성하고 고양이 이미지 지정 */
    .stApp::before {
        content: "";
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        /* 💡 고양이 이미지 URL (Pixabay 공용 이미지) */
        background-image: url("https://cdn.pixabay.com/photo/2016/03/30/17/57/cat-1292023_1280.jpg"); 
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
        background-position: center;
        opacity: 0.25; /* 배경 이미지 투명도 조절 (0.0~1.0, 숫자가 낮을수록 희미함) */
        z-index: -1; /* 다른 콘텐츠 아래로 보내 배경 역할만 하도록 설정 */
    }

    /* 메인 콘텐츠 영역의 배경을 반투명하게 만들어 텍스트 가독성을 높입니다. */
    div.main {
        background-color: rgba(255, 255, 255, 0.7); /* 흰색 배경에 투명도 70% */
        padding: 20px;
        border-radius: 10px;
    }

    /* Streamlit 헤더와 사이드바 배경도 투명하게 설정 */
    header {
        background-color: rgba(0,0,0,0) !important;
    }
    .css-1d3f8iw, .css-1lcbmhc { /* 사이드바 및 기타 Streamlit 내부 클래스 */
        background-color: rgba(255, 255, 255, 0.5) !important;
    }
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

# 배경 이미지 설정 함수 호출 (가장 먼저 실행)
set_background_image_strict()

# --- 웹 앱 주요 기능 시작 ---

# 1. 제목 설정
st.title("💖 헬로 월드 고양이 앱 🐈")

# 2. 사용자 이름 입력 받기
# st.text_input 위젯을 사용하여 사용자의 이름을 입력받습니다.
user_name = st.text_input("당신의 이름은 무엇인가요?", placeholder="여기에 이름을 입력하세요.")

# 3. "입력" 버튼 생성 및 처리
# st.button 위젯을 사용하여 버튼을 만듭니다.
if st.button("입력 뿅~"):
    if user_name:
        # 사용자 이름이 입력된 경우
        message = f"**{user_name}** 님, **헬로 월드** 메시지를 뿅~ 하며 출력했습니다! ✨"
        st.success(message) # 성공 메시지 스타일로 출력
        st.balloons() # 풍선 효과 추가
    else:
        # 사용자 이름이 입력되지 않은 경우 경고 메시지 출력
        st.warning("이름을 먼저 입력해 주세요! 🐱")
