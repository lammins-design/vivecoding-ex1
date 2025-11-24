# app.py

import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu
import numpy as np

# --- 1. 초기 설정 및 데이터 정의 ---

# 1. 스트림릿을 사용해서 웹앱을 만들거야
st.set_page_config(
    page_title="MBTI World Explorer",
    page_icon="🌍",
    layout="wide",
)

# MBTI 목록
MBTI_TYPES = [
    "선택하세요",
    "INFJ", "ISFJ", "INTP", "ISFP", "ENTP", "INFP", "ENTJ", "ISTP",
    "INTJ", "ESFP", "ESTJ", "ENFP", "ESTP", "ISTJ", "ENFJ", "ESFJ"
]

# MBTI 설명 데이터
MBTI_EXPLANATION = {
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

# --- 2. 데이터 로드 및 전처리 ---
@st.cache_data
def load_data():
    """첨부된 CSV 파일을 로드하고 캐싱합니다."""
    try:
        df = pd.read_csv("countriesMBTI_16types.csv")
        df.set_index('Country', inplace=True)
        return df, True
    except FileNotFoundError:
        st.error("❌ 'countriesMBTI_16types.csv' 파일을 찾을 수 없습니다. 파일을 `app.py`와 같은 폴더에 위치시켜주세요.")
        return None, False
    except Exception as e:
        st.error(f"❌ 데이터 로드 중 오류 발생: {e}")
        return None, False

df, DATA_LOADED = load_data()


# --- 3. 통계 분석 및 시각화 함수 ---

def generate_insights(df: pd.DataFrame, mbti_type: str):
    """선택된 MBTI에 대한 통계 분석 및 맞춤 멘트 생성"""
    if not DATA_LOADED or mbti_type not in df.columns:
        return {"ment": "데이터 로드 또는 MBTI 유형 확인에 문제가 있습니다.", "countries": []}

    avg_percentage = df[mbti_type].mean() * 100
    highest_country = df[mbti_type].idxmax()
    highest_percentage = df[mbti_type].max() * 100
    lowest_country = df[mbti_type].idxmin()
    lowest_percentage = df[mbti_type].min() * 100
    top_5_countries = df[mbti_type].nlargest(5).index.tolist()
    
    # 3. 첨부한 파일을 활용해서 사용자가 선택한 MBTI에 대한 통계 정보를 보여주고 그에 걸맞는 멘트를 만들어서 보여줘
    ment = f"""
    ### 🌟 당신의 {mbti_type} 유형에 대한 심층 분석 🌟
    
    당신이 속한 **{mbti_type} ({MBTI_EXPLANATION[mbti_type]['name']})** 유형은 
    전 세계 국가 데이터에서 평균적으로 약 **{avg_percentage:.2f}%**의 비율을 보입니다.
    
    가장 높은 비율을 보이는 나라는 **{highest_country}**로 약 **{highest_percentage:.2f}%**이며, 
    가장 낮은 비율을 보이는 나라는 **{lowest_country}**로 약 **{lowest_percentage:.2f}%**입니다.
    
    **데이터 기반의 맞춤 멘트:**
    당신은 **{mbti_type}** 유형의 특성으로 미루어 볼 때, 이 유형이 특히 많이 분포하는 
    **{', '.join(top_5_countries)}** 와 같은 국가에서 문화적 동질감을 느낄 가능성이 높습니다! 🗺️
    
    """
    
    return {"ment": ment, "top_5_countries": top_5_countries}

def create_mbti_bar_chart(df: pd.DataFrame, mbti_type: str):
    """선택된 MBTI의 국가별 분포를 보여주는 바 차트 생성"""
    plot_df = df[[mbti_type]].sort_values(by=mbti_type, ascending=False).reset_index()
    plot_df.columns = ['Country', 'Percentage']
    plot_df['Percentage'] = plot_df['Percentage'] * 100 

    # 5. 다양하고 멋지고 많이 사용하는 라이브러리 (Plotly)를 적용해서 삐까뻔쩍하게 만들어줘
    fig = px.bar(
        plot_df.head(20), # 상위 20개 국가만 시각화
        x='Country',
        y='Percentage',
        title=f"📈 **{mbti_type} ({MBTI_EXPLANATION[mbti_type]['name']})** 유형의 국가별 분포 (상위 20개국)",
        labels={'Percentage': '비율 (%)', 'Country': '국가'},
        color='Percentage',
        color_continuous_scale=px.colors.sequential.Viridis,
    )
    fig.update_layout(
        xaxis={'categoryorder':'total descending'},
        height=500,
        font=dict(size=14),
    )
    return fig

# --- 4. 페이지 구성 함수 ---

def home_page():
    """앱의 홈 페이지 내용을 렌더링합니다."""
    st.title("🌍 MBTI World Explorer")
    st.markdown("---")

    col1, col2 = st.columns([1, 2])

    with col1:
        st.header("👋 시작하기")
        
        # 4. 처음 접속했을 때는 아무 MBTI가 선택되어 있고 MBTI를 선택하라는 메시지가 나오게 해줘
        st.info("상단의 **MBTI 정보 탐색** 메뉴를 선택하고, 그 안에서 당신의 MBTI를 선택하여 전 세계 통계 정보를 확인해보세요!")
        st.write("")
        
        # '선택하세요'가 기본값인 selectbox (유도용)
        selected_mbti = st.selectbox(
            "👇 당신의 MBTI는 무엇인가요?",
            options=MBTI_TYPES,
            index=0, 
            key='home_mbti_select'
        )

        if selected_mbti != "선택하세요":
            st.markdown(f"""
            ### **{selected_mbti}** 유형을 선택하셨군요!
            이제 상단의 **'🧠 MBTI 정보 탐색'** 메뉴를 클릭해서 상세 정보를 확인해보세요.
            """)
        else:
            st.warning("MBTI를 선택하여 상세 정보를 확인해 보세요.")

    with col2:
        st.header("🧐 MBTI란?")
        st.markdown("""
        **MBTI (Myers-Briggs Type Indicator)**는 개인이 선호하는 네 가지 심리적 선호 지표를 조합하여 **16가지 성격 유형** 중 하나로 분류하는 성격 유형 지표입니다.
        
        * **E** (외향) vs **I** (내향)
        * **S** (감각) vs **N** (직관)
        * **T** (사고) vs **F** (감정)
        * **J** (판단) vs **P** (인식)
        
        
        
        이 앱에서는 각 유형에 대한 설명과 함께, **전 세계 국가별 MBTI 통계 데이터**를 활용하여 흥미로운 정보를 제공합니다.
        """)

def mbti_info_page():
    """MBTI 정보 탐색 페이지 내용을 렌더링합니다."""
    st.title("🧠 MBTI 정보 탐색")
    st.markdown("---")
    
    # 2. 사용자에게 MBTI 를 선택하게 해서
    # 5. 다양하고 멋지고 많이 사용하는 라이브러리 (streamlit-option-menu) 적용
    # 6. 아이콘셋 라이브러리도 설치해서 최대한 그림을 많이 사용해줘 (Bootstrap Icons 활용)
    selected_mbti = option_menu(
        menu_title="MBTI 유형 선택",
        options=MBTI_TYPES,
        icons=["geo-alt-fill"] + ["person-circle-fill"] * 16,
        default_index=0, 
        orientation="horizontal",
        key="mbti_select_menu",
        styles={
            "container": {"padding": "0!important", "background-color": "#fafafa"},
            "icon": {"color": "#0288d1", "font-size": "20px"},
            "nav-link": {"font-size": "16px", "text-align": "center", "margin":"0px", "--hover-color": "#eee"},
            "nav-link-selected": {"background-color": "#0288d1", "color": "white"},
        }
    )

    st.markdown("---")
    
    if selected_mbti == "선택하세요":
        # 4. MBTI를 선택하라는 메시지가 나오게 해줘
        st.header("👆 MBTI를 선택해 주세요!")
        st.info("상단의 16가지 유형 중 당신의 MBTI를 선택하시면 상세 정보가 표시됩니다.")
        st.image("https://i.imgur.com/gK9qC5m.png", caption="MBTI 선택을 기다리고 있습니다.", width=500)
    
    elif selected_mbti in MBTI_EXPLANATION and DATA_LOADED:
        
        # 2. 해당하는 MBTI에 대한 설명을 보여줄거야
        mbti_data = MBTI_EXPLANATION[selected_mbti]
        
        st.header(f"✨ {selected_mbti} ({mbti_data['name']}) 유형")
        st.subheader("💡 유형 설명")
        st.markdown(f"> **{mbti_data['desc']}**")
        
        st.markdown("---")
        
        # 3. 첨부한 파일을 활용해서 사용자가 선택한 MBTI에 대한 통계 정보를 보여주고
        st.subheader("📊 전 세계 국가별 통계 분석")
        
        insights = generate_insights(df, selected_mbti)
        
        with st.container(border=True):
            st.markdown(insights["ment"])
        
        # 3. 통계 정보를 보여주고
        st.plotly_chart(create_mbti_bar_chart(df, selected_mbti), use_container_width=True)
        
    elif not DATA_LOADED:
        st.error("데이터 로드에 실패하여 정보를 표시할 수 없습니다. CSV 파일(countriesMBTI_16types.csv)이 동일한 폴더에 있는지 확인해주세요.")
    else:
        st.error(f"선택된 MBTI 유형 ({selected_mbti})에 대한 설명 데이터가 부족합니다.")

# --- 5. 메인 앱 실행 함수 ---

def main_app():
    """메인 페이지 라우팅 및 사이드바 메뉴를 설정합니다."""
    
    # 메인 네비게이션 메뉴 (Streamlit Option Menu 사용) - 페이지 전환 역할
    selected_page = option_menu(
        menu_title=None,
        options=["홈 🏠", "MBTI 정보 탐색 🧠"],
        icons=["house", "brain"],
        default_index=0,
        orientation="horizontal",
        key="main_navigation",
        styles={
            "container": {"padding": "0!important"},
            "icon": {"color": "blue"},
            "nav-link-selected": {"background-color": "#5b92e5"},
        }
    )
    
    st.sidebar.title("📚 MBTI 탐험 메뉴")
    st.sidebar.markdown(f"**현재 페이지:** `{selected_page}`")
    st.sidebar.markdown("---")
    st.sidebar.info("✨ **Streamlit**과 **Plotly**를 활용하여 멋지게 구현되었습니다.")


    # 페이지 렌더링
    if selected_page == "홈 🏠":
        home_page()
    elif selected_page == "MBTI 정보 탐색 🧠":
        mbti_info_page()

if __name__ == "__main__":
    main_app()
