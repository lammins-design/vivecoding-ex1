import streamlit as st
import time

# 배경 이미지 슬라이드 쇼에 사용할 고양이 이미지 5장의 URL 리스트
CAT_IMAGES = [
    "https://cdn.pixabay.com/photo/2016/03/30/17/57/cat-1292023_1280.jpg",
    "https://cdn.pixabay.com/photo/2017/02/20/18/03/cat-2083492_1280.jpg",
    "https://cdn.pixabay.com/photo/2017/07/25/01/22/cat-2536662_1280.jpg",
    "https://cdn.pixabay.com/photo/2018/03/27/18/19/cat-3266673_1280.jpg",
    "https://cdn.pixabay.com/photo/2017/11/06/13/45/cat-2923568_1280.jpg",
]

# 1. 배경 이미지 슬라이드 쇼 CSS 및 HTML 설정 함수
def set_sliding_background_fixed(images):
    # CSS 애니메이션을 생성합니다. 각 이미지는 5초씩 노출됩니다.
    num_images = len(images)
    total_duration = num_images * 5  # 총 25초
    
    # 키프레임 내용 생성
    keyframes_content = ""
    for i in range(num_images):
        start_percent = (i / num_images) * 100
        end_percent = ((i + 1) / num_images) * 100
        
        # 이미지 노출 시작 시점
        keyframes_content += f"""
        {start_percent}% {{ background-image: url('{images[i]}'); }}
        """
        # 이미지 노출 종료 직전 시점 (전환을 위해)
        if i < num_images - 1:
            keyframes_content += f"""
            {end_percent - 0.01}% {{ background-image: url('{images[i]}'); }}
            """
        else: # 마지막 이미지
            keyframes_content += f"""
            99.99% {{ background-image: url('{images[i]}'); }}
            100% {{ background-image: url('{images[0]}'); }} /* 첫 이미지로 돌아가기 */
            """

    css = f"""
    <style>
    /* 1. 키프레임 (Keyframes) 정의 */
    @keyframes imageSlide {{
        {keyframes_content}
    }}

    /* 2. 배경 이미지 레이어 설정 (::before 의사 요소) */
    .stApp::before {{
        content: "";
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw; /* 뷰포트 너비 */
        height: 100vh; /* 뷰포트 높이 */
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
        background-position: center center;
        opacity: 0.25; /* 배경 이미지 투명도 (0.0~1.0, 텍스트 가독성 확보) */
        z-index: -1;
        
        /* 애니메이션 적용: 25초 동안 무한 반복 */
        animation: imageSlide {total_duration}s infinite; 
    }}

    /* 3. 콘텐츠 가독성을 위한 메인 영역 배경 설정 */
    /* Streamlit 메인 콘텐츠 영역 (이전 코드의 'div.main' 대신 새로운 클래스 사용) */
    .st-emotion-cache-1cypcdb {{
        background-color: rgba(255, 255, 255, 0.8) !important; /* 흰색 배경에 투명도 80% */
        padding: 20px;
        border-radius: 10px;
    }}
    
    /* Streamlit 헤더와 사이드바 배경 투명하게 설정 */
    header {{ background-color: rgba(0,0,0,0) !important; }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

# 배경 이미지 설정 함수 호출
set_sliding_background_fixed(CAT_IMAGES)

# --- 웹 앱 주요 기능 시작 ---

# 2. 제목 설정
st.title("💖 슬라이드 배경 고양이 헬로 월드 앱 🐈")

# 3. 사용자 이름 입력 받기
user_name = st.text_input("당신의 이름은 무엇인가요?", placeholder="여기에 이름을 입력하세요.")

# 4. "입력" 버튼 생성 및 처리
if st.button("입력 뿅~"):
    if user_name:
        # 사용자 이름이 입력된 경우
        message = f"**{user_name}** 님, **헬로 월드** 메시지를 뿅~ 하며 출력했습니다! ✨"
        st.success(message)
        st.balloons()
    else:
        # 사용자 이름이 입력되지 않은 경우 경고 메시지 출력
        st.warning("이름을 먼저 입력해 주세요! 🐱")
