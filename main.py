import streamlit as st

# 1. 페이지 구성 설정 및 배경 이미지 CSS 적용
def set_background_image_strict():
    # Streamlit의 메인 컨테이너와 루트 요소에 직접 배경 이미지를 적용합니다.
    # ::before 의사 요소를 사용하여 배경 레이어를 생성하고 전체 화면을 덮습니다.
    # opacity를 0.9로 설정하여 텍스트 가독성을 높였습니다.
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
        background-image: url("https://cdn.pixabay.com/photo/2016/03/30/17/57/cat-1292023_1280.jpg"); 
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
        background-position: center;
        opacity: 0.25; /* 배경 이미지 투명도 (이 값을 낮추면 배경이 희미해짐) */
        z-index: -1; /* 다른 콘텐츠 아래로 보내기 */
    }

    /* 메인 콘텐츠 영역의 배경을 반투명하게 만들어 텍스트 가독성 높임 */
    div.main {
        background-color: rgba(255, 255, 255, 0.7); /* 흰색 배경에 투명도 70% */
        padding: 20px;
        border-radius: 10px;
    }

    /* 헤더와 사이드바 배경도 투명하게 설정 */
    header {
        background-color: rgba(0,0,0,0) !important;
    }
    .css-1d3f8iw, .css-1lcbmhc { /* 사이드바 및 기타 Streamlit 내부 클래스 */
        background-color: rgba(255, 255, 255, 0.5) !important;
    }
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

# 배경 이미지 설정 함수 호출 (코드의 최상단에서 실행)
set_background_image_strict()

---

## 💻 앱 기능

st.title("💖 헬로 월드 고양이 앱 🐈")

# 2. 사용자 이름 입력 받기
user_name = st.text_input("당신의 이름은 무엇인가요?", placeholder="여기에 이름을 입력하세요.")

#
