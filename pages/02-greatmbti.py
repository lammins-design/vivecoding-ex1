# 01_🏠_홈.py

import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd # 세션 상태를 위해 임포트

# --- 세션 상태 및 초기 설정 ---
st.set_page_config(
    page_title="MBTI World Explorer",
    page_icon="🌍",
    layout="wide",
)

# MBTI 목록 및 설명 데이터 정의 (다른 페이지에서도 접근 가능하도록 세션 상태에 저장)
if 'mbti_types' not in st.session_state:
    st.session_state.mbti_types = [
        "선택하세요",
        "INFJ", "ISFJ", "INTP", "ISFP", "ENTP", "INFP", "ENTJ", "ISTP",
        "INTJ", "ESFP", "ESTJ", "ENFP", "ESTP", "ISTJ", "ENFJ", "ESFJ"
    ]
if 'mbti_explanation' not in st.session_state:
    st.session_state.mbti_explanation = {
        "INFJ": {"name": "옹호자", "desc": "조용하고 신비로우며 지칠 줄 모르는 이상주의자입니다. 사람들을 돕고 세상을 더 좋게 만들고자 하는 깊은 소망을 가지고 있습니다."},
        "ISFJ": {"name": "수호자", "desc": "헌신적이며, 매우 따뜻하고 책임감이 강합니다. 전통을 존중하며 사람들에게 봉사하는 데 기쁨을 느낍니다."},
        "INTP": {"name": "논리술사", "desc": "지적 호기심이 많고 문제 해결에 능숙합니다. 논리와 분석을 통해 세상을 이해하려 합니다."},
        "ISFP": {"name": "모험가", "desc": "유연하고 매력적인 예술가 유형입니다. 현재를 즐기며 자신의 감정을 예술로 표현하는 것을 좋아합니다."},
        "ENTP": {"name": "변론가", "desc": "똑똑하고 호기심이 많으며 도전을 즐깁니다. 논쟁과 토론을 통해 새로운 아이디어를 탐구하는 것을 좋아합니다."},
        "INFP": {"name": "중재자", "desc": "이상적이며, 조용하고 사려 깊은 유형입니다. 자신의 가치관에 따라 세상을 더 아름답게 만들고자 합니다."},
        "ENTJ": {"name": "대담한 통솔자", "desc": "카리스마 있고 자신감이 넘치며 목표 달성을 위해 계획을 세우고 이끄는 데 능숙합니다."},
        "ISTP": {"name": "만능 재주꾼", "desc": "실용적이며 문제 해결 능력이 뛰어납니다. 새로운 도구와 기술을 배우고 직접 체험하는 것을 즐깁니다."},
        "INTJ": {"name": "건축가", "desc": "분석적이고 전략적이며 지능적인 계획가입니다. 지식과 논리를 기반으로 장기적인 비전을 추구합니다."},
        "ESFP": {"name": "연예인", "desc": "즉흥적이고 에너지가 넘치며 주변 사람들에게 즐거움을 선사합니다. 삶을 하나의 파티로 생각합니다."},
        "ESTJ": {"name": "경영자", "desc": "체계적이며, 효율성과 질서를 중요시합니다. 명확한 규칙과 전통을 따르는 데 능숙합니다."},
        "ENFP": {"name": "활동가", "desc": "열정적이고 창의적이며 사회성이 뛰어납니다. 새로운 가능성을 탐색하고 사람들과 깊은 관계를 맺는 것을 좋아합니다."},
        "ESTP": {"name": "사업가", "desc": "에너지가 넘치고 관찰력이 뛰어나며 행동 지향적입니다. 문제에 직접 부딪혀 해결하는 것을 선호합니다."},
        "ISTJ": {"name": "현실주의자", "desc": "책임감이 강하고 사실에 입각하여 신뢰할 수 있습니다. 체계적인 방식으로 업무를 처리합니다."},
        "ENFJ": {"name": "선도자", "desc": "타인을 이끌고 영감을 주는 데 능숙한 카리스마 넘치는 지도자입니다. 사람들의 잠재력을 끌어내는 것을 좋아합니다."},
        "ESFJ": {"name": "친선도모자", "desc": "사교성이 뛰어나고 따뜻하며 다른 사람들의 필요를 잘 챙깁니다. 공동체 의식을 중요시합니다."},
    }

# --- 홈 페이지 내용 ---
st.title("🌍 MBTI World Explorer")
st.markdown("---")

col1, col2 = st.columns([1, 2])

with col1:
    st.header("👋 시작하기")
    st.info("좌측 사이드바의 **'MBTI 정보 탐색'** 페이지에서 당신의 MBTI를 선택하고 전 세계 통계 정보를 확인해보세요!")
    st.write("")
    # MBTI 선택 드롭다운 (초기 상태 유지를 위한)
    selected_mbti = st.selectbox(
        "👇 당신의 MBTI는 무엇인가요?",
        options=st.session_state.mbti_types,
        index=0, # '선택하세요'가 기본값
        key='home_mbti_select'
    )

    if selected_mbti != "선택하세요":
        st.markdown(f"""
        ### **{selected_mbti}** 유형을 선택하셨군요!
        이제 좌측 사이드바에서 **'🧠 MBTI 정보 탐색'** 페이지로 이동해서 상세 정보를 확인해보세요.
        """)
    else:
        # 4. 처음 접속했을 때는 아무 MBTI가 선택되어 있고 MBTI를 선택하라는 메시지가 나오게 해줘
        st.warning("MBTI를 선택하여 상세 정보를 확인해 보세요.")


with col2:
    st.header("🧐 MBTI란?")
    st.markdown("""
    **MBTI (Myers-Briggs Type Indicator)**는 개인이 선호하는 네 가지 심리적 선호 지표를 조합하여 **16가지 성격 유형** 중 하나로 분류하는 성격 유형 지표입니다.
    
    * **E** (외향) vs **I** (내향) - 에너지의 방향
    * **S** (감각) vs **N** (직관) - 정보 인식 방법
    * **T** (사고) vs **F** (감정) - 의사결정 방법
    * **J** (판단) vs **P** (인식) - 생활 양식
    
    이 앱에서는 각 유형에 대한 설명과 함께, **전 세계 국가별 MBTI 통계 데이터**를 활용하여 흥미로운 정보를 제공합니다.
    """)
