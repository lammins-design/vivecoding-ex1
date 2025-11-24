import streamlit as st
import pandas as pd
import numpy as np

# --- 1. 데이터 로드 및 전처리 ---
# 업로드된 CSV 파일 경로를 사용합니다.
FILE_PATH = "countriesMBTI_16types.csv"

@st.cache_data
def load_data(file_path):
    """CSV 파일을 로드하고 필요한 전처리를 수행합니다."""
    try:
        df = pd.read_csv(file_path)
        # 국가(Country) 열을 인덱스로 설정
        df = df.set_index('Country')
        # MBTI 유형 목록 추출
        mbti_types = df.columns.tolist()
        return df, mbti_types
    except FileNotFoundError:
        st.error(f"⚠️ 오류: 파일을 찾을 수 없습니다. 경로를 확인해주세요: {file_path}")
        return pd.DataFrame(), []
    except Exception as e:
        st.error(f"⚠️ 오류: 데이터 로드 중 문제가 발생했습니다: {e}")
        return pd.DataFrame(), []

data_df, mbti_list = load_data(FILE_PATH)

# MBTI 유형별 설명을 정의하는 딕셔너리
mbti_descriptions = {
    "INTJ": "용의주도한 전략가 (Architect). 상상력이 풍부하며, 모든 일에 계획을 세우는 분석적인 성격입니다.",
    "INTP": "논리적인 사색가 (Logician). 끊임없이 지식을 탐구하며, 지적인 호기심이 강한 철학자입니다.",
    "ENTJ": "대담한 통솔자 (Commander). 비전을 제시하고, 사람들을 이끌어 목표를 달성하는 타고난 지도자입니다.",
    "ENTP": "뜨거운 논쟁을 즐기는 변론가 (Debater). 지적인 도전을 즐기며, 현 상태를 뒤집는 아이디어를 제시합니다.",
    "INFJ": "선의의 옹호자 (Advocate). 깊은 통찰력과 온정적인 마음을 가진, 세상을 이롭게 하려는 이상주의자입니다.",
    "INFP": "열정적인 중재자 (Mediator). 헌신적이고 이타적이며, 의미 있는 삶을 추구하는 진정한 이상주의자입니다.",
    "ENFJ": "정의로운 사회운동가 (Protagonist). 카리스마와 영감을 불어넣는 지도자로, 사람들의 성장을 돕습니다.",
    "ENFP": "재기발랄한 활동가 (Campaigner). 창의적이고 사교적이며, 삶을 즐기는 자유로운 영혼의 소유자입니다.",
    "ISTJ": "청렴결백한 논리주의자 (Logistician). 사실에 근거하여 책임감 있게 행동하는 실용적인 관리자입니다.",
    "ISFJ": "용감한 수호자 (Defender). 사려 깊고 헌신적이며, 타인을 보호하고 돕는 조용하고 따뜻한 성격입니다.",
    "ESTJ": "엄격한 관리자 (Executive). 체계적이고 조직적이며, 규칙을 준수하고 사람들을 이끄는 효율적인 관리자입니다.",
    "ESFJ": "사교적인 외교관 (Consul). 배려심이 깊고 사람들을 좋아하며, 사회적 조화를 중시하는 인기 있는 성격입니다.",
    "ISTP": "만능 재주꾼 (Virtuoso). 대담하고 현실적이며, 손으로 직접 만들고 실험하는 것을 즐기는 장인입니다.",
    "ISFP": "호기심 많은 예술가 (Adventurer). 유연하고 매력적이며, 새로운 것을 탐험하며 예술적인 삶을 사는 모험가입니다.",
    "ESTP": "모험을 즐기는 사업가 (Entrepreneur). 에너지 넘치고 즉흥적이며, 현실적인 문제 해결 능력이 뛰어난 활동가입니다.",
    "ESFP": "자유로운 영혼의 연예인 (Entertainer). 즉흥적이고 활기차며, 주변 사람들을 즐겁게 하는 타고난 엔터테이너입니다."
}

# --- 2. Streamlit 앱 레이아웃 설정 ---
st.set_page_config(page_title="MBTI 유형 분석 웹 앱", layout="centered")

st.title("🧠 MBTI 유형 분석 & 글로벌 통계 정보")
st.markdown("---")

# --- 3. 사용자 입력 (MBTI 선택) ---
# 초기 선택 상태: 아무것도 선택하지 않음
if 'selected_mbti' not in st.session_state:
    st.session_state.selected_mbti = None
    
# 초기 메시지
initial_message = "👈 왼쪽 사이드바에서 **당신의 MBTI 유형**을 선택해주세요!"

# 사이드바에 셀렉트 박스 추가
selected_mbti = st.sidebar.selectbox(
    "MBTI 유형을 선택하세요:",
    options=["MBTI를 선택하세요..."] + mbti_list,
    index=0,  # 초기값은 "MBTI를 선택하세요..."
    key="selectbox_mbti"
)

# 셀렉트 박스에서 MBTI 유형을 실제로 선택했을 때만 상태 업데이트
if selected_mbti != "MBTI를 선택하세요...":
    st.session_state.selected_mbti = selected_mbti
else:
    # "MBTI를 선택하세요..." 상태일 때만 초기 메시지를 보여줍니다.
    if st.session_state.selected_mbti is None:
        st.info(initial_message)


# --- 4. 선택된 MBTI 정보 표시 ---
if st.session_state.selected_mbti and st.session_state.selected_mbti in mbti_descriptions:
    mbti = st.session_state.selected_mbti

    ## 4.1 MBTI 유형 설명
    st.header(f"✨ **선택된 유형: {mbti}**")
    st.subheader(mbti_descriptions.get(mbti, "설명을 찾을 수 없습니다."))
    st.markdown("---")

    ## 4.2 글로벌 통계 분석
    st.header("🌎 글로벌 통계 분석 (국가별 분포)")
    
    if not data_df.empty and mbti in data_df.columns:
        # 해당 MBTI 유형의 국가별 분포 데이터 추출 및 정렬
        mbti_data = data_df[mbti].sort_values(ascending=False)
        
        # 상위 5개 국가
        top_5_countries = mbti_data.head(5)
        
        st.markdown(f"**{mbti} 유형**이 **가장 높은 비율**을 보이는 상위 5개 국가:")
        
        # 데이터 프레임을 사용하여 표로 깔끔하게 표시
        st.dataframe(
            top_5_countries.reset_index().rename(columns={'Country': '국가', mbti: '비율'}),
            use_container_width=True,
            hide_index=True,
            column_config={
                "비율": st.column_config.ProgressColumn(
                    "비율",
                    help="해당 MBTI 유형이 국가 전체 인구에서 차지하는 비율",
                    format="%.2f", # 소수점 두 자리까지 표시
                    min_value=0,
                    max_value=mbti_data.max()
                )
            }
        )
        
        # 통계 기반 멘트 생성
        top_country = top_5_countries.index[0]
        top_ratio = top_5_countries.iloc[0] * 100 # 비율을 퍼센트로 변환
        
        # 멘트 생성
        if top_ratio > 10:
            comment = f"**{mbti}** 유형은 **{top_country}**에서 약 **{top_ratio:.2f}%**로 매우 두드러지게 나타나네요! 당신의 유형은 이 국가의 문화나 성향과 특히 잘 맞을 수 있습니다."
        elif top_ratio > 5:
            comment = f"**{mbti}** 유형은 **{top_country}**에서 약 **{top_ratio:.2f}%**를 차지하며, 이 국가에서 비교적 흔한 유형입니다. 당신과 비슷한 성향의 사람들이 많을 수 있습니다!"
        else:
            comment = f"**{mbti}** 유형은 **{top_country}**에서 약 **{top_ratio:.2f}%**로, 글로벌하게 희귀하거나 특정 국가에서 두드러지지 않는 독특한 유형일 수 있습니다. 특별한 당신의 성향을 응원합니다!"
            
        st.success(f"🌟 통계 맞춤 멘트:\n\n{comment}")
        
    else:
        st.warning("선택하신 MBTI 유형에 대한 통계 데이터를 처리할 수 없습니다.")
        
# --- 5. 미선택 상태 메시지 유지 (초기 접속 시) ---
elif st.session_state.selected_mbti is None:
    # 이미 초기 메시지가 위에서 표시되었으므로 추가적인 메시지는 출력하지 않습니다.
    pass
