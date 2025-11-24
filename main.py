import streamlit as st

# 1. 페이지 구성 설정 (배경 이미지 추가를 위해 사용)
# Streamlit 기본 레이아웃은 커스텀 CSS를 사용하여 배경 이미지를 설정합니다.
# 이미지 URL은 고양이 이미지를 제공하는 공용 URL을 사용했습니다.
# 필요에 따라 다른 고양이 이미지 URL로 변경할 수 있습니다.
def set_background_image():
    # 투명도(opacity: 0.2)를 낮춰 텍스트가 잘 보이도록 했습니다.
    css = """
    <style>
    .stApp {
        background-image: url("https://cdn.pixabay.com/photo/2016/03/30/17/57/cat-1292023_1280.jpg"); 
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
        background-position: center;
        opacity: 0.9; /* 배경 이미지 투명도 조절 */
    }
    .stApp > header {
        background-color: rgba(0,0,0,0); /* 헤더 배경 투명하게 */
    }
    .main > div {
        background-color: rgba(255, 255, 255, 0.7); /* 메인 콘텐츠 영역 배경을 반투명 흰색으로 */
        padding: 20px;
        border-radius: 10px;
    }
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

# 배경 이미지 설정 함수 호출
set_background_image()

## 웹 앱 주요 기능
# 2. 제목 설정
st.title("💖 헬로 월드 고양이 앱 🐈")

# 3. 사용자 이름 입력 받기
# st.text_input 위젯을 사용하여 사용자의 이름을 입력받습니다.
user_name = st.text_input("당신의 이름은 무엇인가요?", placeholder="여기에 이름을 입력하세요.")

# 4. "입력" 버튼 생성
# st.button 위젯을 사용하여 버튼을 만듭니다. 버튼이 클릭되면 True를 반환합니다.
if st.button("입력 뿅~"):
    # 5. 버튼 클릭 시 메시지 출력
    if user_name:
        # 사용자 이름이 입력된 경우
        message = f"**{user_name}** 님, **헬로 월드** 메시지를 뿅~ 하며 출력했습니다! ✨"
        st.success(message) # 성공 메시지 스타일로 출력
    else:
        # 사용자 이름이 입력되지 않은 경우 경고 메시지 출력
        st.warning("이름을 먼저 입력해 주세요! 🐱")
        
#
