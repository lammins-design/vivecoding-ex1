import streamlit as st
import time # 슬라이드 쇼를 제어하기 위해 사용되지는 않지만, Streamlit 앱의 일반적인 라이브러리입니다.

# 1. 배경 이미지 슬라이드 쇼 CSS 및 HTML 설정 함수
def set_sliding_background():
    # 고양이 이미지 5장의 공용 URL 리스트입니다.
    # 이미지가 로드되지 않을 경우를 대비해 다양한 소스의 이미지를 사용합니다.
    cat_images = [
        "https://cdn.pixabay.com/photo/2016/03/30/17/57/cat-1292023_1280.jpg",        # 1. 아웃포커싱 고양이
        "https://cdn.pixabay.com/photo/2017/02/20/18/03/cat-2083492_1280.jpg",        # 2. 풀밭 고양이
        "https://cdn.pixabay.com/photo/2017/07/25/01/22/cat-2536662_1280.jpg",        # 3. 누워있는 고양이
        "https://cdn.pixabay.com/photo/2018/03/27/18/19/cat-3266673_1280.jpg",        # 4. 카메라 보는 고양이
        "https://cdn.pixabay.com/photo/2017/11/06/13/45/cat-2923568_1280.jpg",        # 5. 아기고양이
    ]

    # CSS 애니메이션을 사용하여 배경 이미지를 순차적으로 전환합니다.
    # 각 이미지는 5초씩 노출되고, 전체 애니메이션 사이클은 25초입니다 (5장 * 5초).
    css = f"""
    <style>
    /* 1. 키프레임 (Keyframes) 정의: 배경 이미지 전환 애니메이션 */
    @keyframes imageSlide {
        0% {{ background-image: url('{cat_images[0]}'); }} /* 0%~20% (5초) */
        19.99% {{ background-image: url('{cat_images[0]}'); }}
        
        20% {{ background-image: url('{cat_images[1]}'); }} /* 20%~40% (5초) */
        39.99% {{ background-image: url('{cat_images[1]}'); }}

        40% {{ background-image: url('{cat_images[2]}'); }} /* 40%~60% (5초) */
        59.99% {{ background-image: url('{cat_images[2]}'); }}

        60% {{ background-image: url('{cat_images[3]}'); }} /* 60%~80% (5초) */
        79.99% {{ background-image: url('{cat_images[3]}'); }}

        80% {{ background-image: url('{cat_images[4]}'); }} /* 80%~100% (5초) */
        99.99% {{ background-image: url('{cat_images[4]}'); }}
        100% {{ background-image: url('{cat_images[0]}'); }} /* 마지막 이미지를 보여준 후, 0%로 돌아가 반복 */
    }}

    /* 2. 배경 이미지를 담을 ::before 요소 설정 */
    .stApp::before {{
        content: "";
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
        background-position: center;
        opacity: 0.3; /* 배경 이미지 투명도 (텍스트 가독성 확보) */
        z-index: -1;
        
        /* 애니메이션 적용 */
        animation: imageSlide 25s infinite; /* 25초 동안 애니메이션을 무한 반복 */
    }}

    /* 3. 콘텐츠 가독성을 위한 메인 영역 배경 설정 */
    div.main {{
        background-color: rgba(255, 255, 255, 0.7); /* 흰색 배경에 투명도 70% */
        padding: 20px;
        border-radius: 10px;
    }}
    header {{ background-color: rgba(0,0,0,0) !important; }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

# 배경 이미지 설정 함수 호출
set_sliding_background()

# --- 웹 앱 주요 기능 시작 ---

# 2. 제목 설정
st.title("💖 슬라이드 배경 고양이 헬로 월드 앱 🐈")

# 3. 사용자 이름 입력 받기
user_name = st.text_input("당신의 이름은 무엇인가요?", placeholder="여기에 이름을 입력하세요.")

# 4. "입력" 버튼 생성 및 처리
if st.button("입력 뿅~"):
    if user_name:
        message = f"**{user_name}** 님, **헬로 월드** 메시지를 뿅~ 하며 출력했습니다! ✨"
        st.success(message)
        st.balloons() # 풍선 효과 추가
    else:
        st.warning("이름을 먼저 입력해 주세요! 🐱")
