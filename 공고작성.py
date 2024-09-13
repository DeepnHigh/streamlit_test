import streamlit as st
import pyperclip
from datetime import datetime


if 'braincore' not in st.session_state:
    st.session_state['braincore'] = ""
st.session_state['braincore'] = """
            주식회사 브레인코어는 AI 교육과 에듀테크 분야에서 앞서 나가는 혁신적인 기업입니다. 
            우리는 성인과 청소년을 대상으로 인공지능 교육 프로그램을 개발하고 제공하며, 이를 통해 AI 기술의 대중화를 촉진하고 있습니다.
    
            * 인공지능 교육 프로그램 개발: 다양한 연령대의 학습자를 위한 맞춤형 AI 교육 콘텐츠를 제공합니다.
            * 에듀테크 솔루션 제공: 기술 기반의 교육 솔루션을 통해 학습 효율성을 극대화합니다.
            * 유연한 근무 환경: 자율출퇴근제를 포함한 직원 복지를 강화하여 창의적이고 자율적인 업무 환경을 조성합니다."""

if 'neotech' not in st.session_state:
    st.session_state['neotech'] = ""
st.session_state['neotech'] = """
            주식회사 네오텍솔루션은 AI 기반의 스마트 제조 시스템과 혁신적인 자동화 솔루션을 제공하는 선도적인 제조업 기업입니다. 
            우리는 다양한 산업 분야에 맞춤형 제조 솔루션을 제공하여 생산성을 극대화하고, 지속 가능한 제조 환경을 구축하는 데 기여하고 있습니다.

            * 스마트 제조 시스템 개발: AI와 IoT 기술을 결합한 스마트 공정 관리 시스템을 통해 생산 라인의 효율성을 극대화합니다.
            * 자동화 솔루션 제공: 로봇 공학과 첨단 자동화 기술을 활용하여 작업 환경을 개선하고 인건비 절감을 돕습니다.
            * 지속 가능한 제조: 친환경 공정 도입과 자원 절약 기술을 통해 지속 가능한 제조업 환경을 구축합니다. """

if 'green' not in st.session_state:
    st.session_state['green'] = ""
st.session_state['green'] = """
            주식회사 그린메이커스는 지속 가능한 제품과 서비스를 제공하는 친환경 제조업 회사로, 에너지 절감 및 자원 효율성을 극대화하는 혁신적인 솔루션을 개발하고 있습니다. 
            우리는 다양한 산업 분야에서 친환경 기술을 적용하여, 고객에게 고품질의 에너지 절감 제품과 솔루션을 제공하며, 지속 가능한 미래를 위한 제조업 혁신을 선도하고 있습니다.

            * 에너지 절감 제품 개발: 우리는 에너지 소비를 줄일 수 있는 고효율 제품을 설계 및 제조합니다.
            * 지속 가능한 자원 관리: 자원 사용을 최소화하는 프로세스를 개발하여 폐기물 발생을 줄이고, 자원을 효율적으로 관리합니다.
            * 친환경 솔루션 제공: 다양한 산업 현장에 적용 가능한 친환경 공정과 기술을 제공해 환경 보호에 기여합니다. """



if 'business_registration_number' not in st.session_state:
    st.session_state['business_registration_number'] = ""
st.session_state['business_registration_number'] = st.sidebar.text_input("사업자 등록 번호", placeholder = "사업자 등록 번호를 입력해 주세요.",value=st.session_state['business_registration_number'])

if 'job_title' not in st.session_state:
    st.session_state['job_title'] = ""
st.session_state['job_title'] = st.sidebar.text_input("공고명", placeholder = "공고명을 입력해 주세요.",value=st.session_state['job_title'])

if 'job_description' not in st.session_state:
    st.session_state['job_description'] = ""
st.session_state['job_description'] = st.sidebar.text_area("공고 내용", placeholder = "구인 공고에 들어갈 필수적인 내용을 작성해주세요.", height=100, value=st.session_state['job_description'])

welfare_list = ["자율출퇴근제", "유연 근무제", "건강 검진 및 의료 지원", "자기 개발 지원 프로그램", "사내 동호회 및 문화 활동 지원"]

# session state 초기화
if 'welfare' not in st.session_state:
    st.session_state['welfare'] = []
if 'other_welfare' not in st.session_state:
    st.session_state['other_welfare'] = ""
if 'selected_welfare' not in st.session_state:
    st.session_state['selected_welfare'] = []

# multiselect 위젯
st.session_state['welfare'] = st.sidebar.multiselect("혜택 및 복지", welfare_list, default=st.session_state['welfare'])
welfare = st.session_state['welfare']

# 기타 복지 입력 받기
st.session_state['other_welfare'] = st.sidebar.text_input("기타 복지 입력 (쉼표로 구분해서 입력 후 Enter)", value=st.session_state['other_welfare'])
other_welfare = st.session_state['other_welfare']

selected_welfare = []
for item in st.session_state['welfare']:
    selected_welfare.append(item)

#사용자가 입력한 기타 복지를 쉼표로 나눠서 추가
if other_welfare:
    other_welfare_list = [w.strip() for w in other_welfare.split(',')]
    for welfare_item in other_welfare_list:
        if welfare_item and welfare_item not in welfare:
            selected_welfare.append(welfare_item)

# session state 업데이트
st.session_state['selected_welfare'] = selected_welfare

recruitment_list = ["서류 전형", "1차 면접", "2차 면접", "실무진 면접", "입원 면접", "코딩테스트", "최종 합격"]
# session state 초기화
if 'recruitment' not in st.session_state:
    st.session_state['recruitment'] = []
if 'other_recruitment' not in st.session_state:
    st.session_state['other_recruitment'] = ""
if 'selected_recruitment' not in st.session_state:
    st.session_state['selected_recruitment'] = []

# multiselect 위젯
st.session_state['recruitment'] = st.sidebar.multiselect("채용 전형", recruitment_list, default=st.session_state['recruitment'])
recruitment = st.session_state['recruitment']

# 기타 채용 전형 입력 받기
st.session_state['other_recruitment'] = st.sidebar.text_input("기타 채용 전형 입력 (쉼표로 구분해서 입력 후 Enter)", value=st.session_state['other_recruitment'])
other_recruitment = st.session_state['other_recruitment']

selected_recruitment = []
for item in st.session_state['recruitment']:
    selected_recruitment.append(item)

#사용자가 입력한 기타 복지를 쉼표로 나눠서 추가
if other_recruitment:
    other_recruitment_list = [w.strip() for w in other_recruitment.split(',')]
    for recruitment_item in other_recruitment_list:
        if recruitment_item and recruitment_item not in recruitment:
            selected_recruitment.append(recruitment_item)

# session state 업데이트
st.session_state['selected_recruitment'] = selected_recruitment

# 톤 선택 라디오 버튼 (사이드바)
tone = st.sidebar.radio("톤 선택", ("격식있게", "친근하게"))




# 키워드 선택 상태를 저장하기 위해 session_state 사용
if 'keyword_generation' not in st.session_state:
    st.session_state['keyword_generation'] = False

if 'keywords' not in st.session_state:
    st.session_state['keywords'] = [False, False, False, False, False]

# 키워드 생성 버튼을 클릭할 때 상태를 True로 변경
if st.sidebar.button('✨ 키워드 생성', key='keyword_generation_btn'):
    st.session_state['keyword_generation'] = True



# 세션 상태에서 기본 텍스트가 없는 경우 초기화
if 'text' not in st.session_state:
    st.session_state['text'] = ""
    st.session_state['company_introduction_text'] = ""
    st.session_state['major_task_text'] = ""
    st.session_state['qualification_requirements_text'] = ""
    st.session_state['benefits_and_welfare_text'] = ""
    st.session_state['recruitment_text'] = ""
    st.session_state['skill_text'] = ""



### 인공지능 교육 강사 케이스
if st.session_state['business_registration_number'] == "111-11-11111":

    if st.session_state['keyword_generation']:
        st.subheader("브레인 코어")
        st.text_area("회사 소개", st.session_state['braincore'], height=200)
        st.subheader("공고 기반 키워드 선택")

        col1, col2, col3, col4, col5 = st.columns(5)
    # 각 키워드 선택 상태를 체크박스로 표시
        with col1:
            st.session_state['keywords'][0] = st.checkbox('인공지능 교육', value=st.session_state['keywords'][0], key='kw1')
            if st.session_state['keywords'][0]:
                st.session_state['keywords'][0] = "인공지능 교육"
        with col2:
            st.session_state['keywords'][1] = st.checkbox('초·중등 교육', value=st.session_state['keywords'][1], key='kw2')
            if st.session_state['keywords'][1]:
                st.session_state['keywords'][1] = "초·중등 교육"
        with col3:
            st.session_state['keywords'][2] = st.checkbox('강사 모집', value=st.session_state['keywords'][2], key='kw3')
            if st.session_state['keywords'][2]:
                st.session_state['keywords'][2] = "강사 모집"
        with col4:
            st.session_state['keywords'][3] = st.checkbox('교통비 및 교재 지원', value=st.session_state['keywords'][3], key='kw4')
            if st.session_state['keywords'][3]:
                st.session_state['keywords'][3] = "교통비 및 교재 지원"
        with col5:
            st.session_state['keywords'][4] = st.checkbox('수업 시연 전형', value=st.session_state['keywords'][4], key='kw5')
            if st.session_state['keywords'][4]:
                st.session_state['keywords'][4] = "수업 시연 전형"

        col1, col2, col3 = st.columns(3)
        with col2:
            # CSS 스타일로 버튼 크기 조절
            st.markdown("""
                <style>
                div.stButton > button {
                    font-size: 100px;
                    padding: 10px 20px;
                    width: 100%; /* 버튼을 가로로 꽉 채움 */
                }
                </style>
                """, unsafe_allow_html=True)

            # 버튼 생성
            if st.button("✨ 공고 생성", key='generate_btn'):

                st.session_state['text'] = True
                st.session_state['company_introduction_text'] = """    
            주식회사 브레인코어는 초·중등 학생들을 대상으로 인공지능(AI) 교육을 기획하고 진행할 유능한 강사를 모집하고 있습니다. 
            이 직무는 학생들이 인공지능 기술을 이해하고 실생활에 응용할 수 있도록 돕는 역할을 담당합니다. 
            주 강의 대상은 초·중등 학생으로, AI 기초 개념부터 실제 프로그래밍까지 체계적인 교육을 진행하며, 교육 커리큘럼에 맞춘 수업 자료, 교재, 교구재를 준비하게 됩니다. 
            학생들의 학습 수준을 고려하여 맞춤형 수업을 설계하고, 학습 성과를 평가해 효과적인 피드백을 제공합니다.  
            인공지능 교육 트렌드에 맞춰 최신 기술을 반영하여 학생들이 보다 쉽게 AI에 접근할 수 있도록 돕습니다. 
            교육 경력 및 AI 도구 사용 경험을 보유한 분을 우대하며, 창의적인 수업 방식과 원활한 소통 능력도 중요한 자질입니다. 
            다양한 혜택으로는 교통비 지원, 교재 제공, 자율적인 수업 준비 시간, 그리고 교육 관련 세미나 및 워크숍 참여 기회 등이 제공됩니다."""

                st.session_state['major_task_text'] = """ 
            * 초·중등 학생을 대상으로 한 인공지능 교육 기획 및 진행
            * 교육 커리큘럼에 맞춘 수업 자료, 교재 및 교구재 준비
            * 학생들의 이해도를 고려한 맞춤형 수업 설계 및 운영
            * 학생들의 학습 성과에 대한 평가 및 피드백 제공
            * 인공지능 관련 최신 기술 및 교육 트렌드에 대한 정보 업데이트 및 반영"""

                st.session_state['qualification_requirements_text'] = """
            * 교육 관련 경력 및 초·중등 학생 대상 수업 경험
            * 인공지능 또는 컴퓨터 과학 분야 전공자 또는 관련 자격증 보유자
            * 파이썬(Python) 및 AI 도구를 활용한 수업 경험
            * 창의적이고 학생 중심의 수업 방식에 대한 이해
            * 원활한 소통 및 협업 능력"""

                st.session_state['benefits_and_welfare_text'] = """
            * 강의장까지 교통비 지원: 강의 장소와 거리에 상관없이 교통비 전액 지원
            * 교재 및 교구재 지원: 강의에 필요한 모든 교재 및 교구재 제공
            * 자율적인 수업 준비 시간 및 유연한 일정 조정 가능
            * 교육 관련 세미나 및 워크숍 참여 기회 제공 """

                st.session_state['recruitment_text'] = """
            * 서류 전형: 제출된 이력서 및 자기소개서를 기반으로 평가
            * 면접: 직무 적합성 및 인성 면접
            * 수업 시연: 실제 교육을 진행하는 방식에 대한 시연 및 피드백 제공
            * 최종 합격: 조건 협의 후 입사"""

                st.session_state['skill_text'] = """
            * 프로그래밍 언어: Python (기본 AI 프로그래밍)
            * 교육 도구: 다양한 AI 교육 플랫폼 및 도구 (Scratch, 구글 Colab 등)
            * 협업 및 관리 도구: Slack, Google Drive, Zoom (원격 교육 시) """

    if st.session_state['text']:
        container1 = st.container(border=True)

        with container1:
            # 회사/직무 소개 섹션
            st.subheader("직무 소개")
            st.session_state['company_introduction_text'] = st.text_area(
                '직무 소개', value=st.session_state['company_introduction_text'], height=250, label_visibility='collapsed'    )

            col1, col2, col3 = st.columns([10, 2.8, 2])

            # 회사/직무 소개 전체 삭제 버튼을 누른 경우 텍스트를 삭제
            with col2:
                if st.button("🗑️ 전체 삭제", key='delete_company_intro'):
                    st.session_state['company_introduction_text'] = ""  # 텍스트 상자 내용을 빈 문자열로 설정
                    st.rerun()


            with col3:
                # 복사 버튼을 누른 경우, 복사 알림 메시지 출력
                if st.button("📄 복사", key='copy_company_intro'):
                    pyperclip.copy(st.session_state['company_introduction_text'])  # 텍스트 복사

            # 주요 업무 섹션
            st.subheader("주요 업무")
            st.session_state['major_task_text'] = st.text_area(
                '주요 업무', value=st.session_state['major_task_text'], height=180, label_visibility='collapsed'
            )

            col1, col2, col3 = st.columns([10, 2.8, 2])

            # 주요 업무 전체 삭제 버튼을 누른 경우 텍스트를 삭제
            with col2:
                if st.button("🗑️ 전체 삭제", key='delete_major_tasks'):
                    st.session_state['major_task_text'] = ""  # 텍스트 상자 내용을 빈 문자열로 설정
                    st.rerun()

            with col3:
                # 복사 버튼을 누른 경우, 복사 알림 메시지 출력
                if st.button("📄 복사", key='copy_major_tasks'):
                    pyperclip.copy(st.session_state['major_task_text'])  # 텍스트 복사


            # 우대사항 섹션
            st.subheader("우대사항")
            st.session_state['qualification_requirements_text'] = st.text_area(
                '우대사항', value=st.session_state['qualification_requirements_text'], height=180, label_visibility='collapsed'
            )

            col1, col2, col3 = st.columns([10, 2.8, 2])

            # 우대사항 전체 삭제 버튼을 누른 경우 텍스트를 삭제
            with col2:
                if st.button("🗑️ 전체 삭제", key='delete_qualification_requirements'):
                    st.session_state['qualification_requirements_text'] = ""  # 텍스트 상자 내용을 빈 문자열로 설정
                    st.rerun()

            with col3:
                # 복사 버튼을 누른 경우, 복사 알림 메시지 출력
                if st.button("📄 복사", key='copy_qualification_requirements'):
                    pyperclip.copy(st.session_state['qualification_requirements_text'])  # 텍스트 복사

            # 혜택 및 복지 섹션
            st.subheader("혜택 및 복지")
            st.session_state['benefits_and_welfare_text'] = st.text_area(
                '혜택 및 복지', value=st.session_state['benefits_and_welfare_text'], height=160, label_visibility='collapsed'
            )

            col1, col2, col3 = st.columns([10, 2.8, 2])

            # 우대사항 전체 삭제 버튼을 누른 경우 텍스트를 삭제
            with col2:
                if st.button("🗑️ 전체 삭제", key='delete_benefits_and_welfare_text'):
                    st.session_state['benefits_and_welfare_text'] = ""  # 텍스트 상자 내용을 빈 문자열로 설정
                    st.rerun()

            with col3:
                # 복사 버튼을 누른 경우, 복사 알림 메시지 출력
                if st.button("📄 복사", key='copy_benefits_and_welfare_text'):
                    pyperclip.copy(st.session_state['benefits_and_welfare_text'])  # 텍스트 복사


            # 채용 전형 섹션
            st.subheader("채용 전형")
            st.session_state['recruitment_text'] = st.text_area(
                '채용 전형', value=st.session_state['recruitment_text'], height=160, label_visibility='collapsed'
            )

            col1, col2, col3 = st.columns([10, 2.8, 2])

            # 우대사항 전체 삭제 버튼을 누른 경우 텍스트를 삭제
            with col2:
                if st.button("🗑️ 전체 삭제", key='delete_recruitment_text'):
                    st.session_state['recruitment_text'] = ""  # 텍스트 상자 내용을 빈 문자열로 설정
                    st.rerun()

            with col3:
                # 복사 버튼을 누른 경우, 복사 알림 메시지 출력
                if st.button("📄 복사", key='copy_recruitment_text'):
                    pyperclip.copy(st.session_state['recruitment_text'])  # 텍스트 복사

            # 채용 전형 섹션
            st.subheader("기술 스택")
            st.session_state['skill_text'] = st.text_area(
                '기술 스택', value=st.session_state['skill_text'], height=140, label_visibility='collapsed'
            )

            col1, col2, col3 = st.columns([10, 2.8, 2])

            # 우대사항 전체 삭제 버튼을 누른 경우 텍스트를 삭제
            with col2:
                if st.button("🗑️ 전체 삭제", key='delete_skill_text'):
                    st.session_state['skill_text'] = ""  # 텍스트 상자 내용을 빈 문자열로 설정
                    st.rerun()

            with col3:
                # 복사 버튼을 누른 경우, 복사 알림 메시지 출력
                if st.button("📄 복사", key='copy_skill_text'):
                    pyperclip.copy(st.session_state['skill_text'])  # 텍스트 복사

        container2 = st.container(border=True)

        with container2:
            # 직군/직무 선택
            st.subheader("직군/직무")

            # 직군 선택 (왼쪽 셀렉트박스)
            if 'job_category' not in st.session_state:
                st.session_state['job_category'] = ""
            st.session_state['job_category'] = st.selectbox("직군", options=["경영·비즈니스", "개발", "디자인", "마케팅", "인사", "운영", "교육"])

            # 직무 선택 (오른쪽 셀렉트박스)
            if 'job_role' not in st.session_state:
                st.session_state['job_role'] = ""
            st.session_state['job_role'] = st.selectbox("직무",
                                                        options=["서비스 기획자", "데이터 분석가", "디자이너", "백엔드 개발자", "프론트엔드 개발자", "인공지능 강사"])

            col1, col2 = st.columns(2)
            with col1:
                if 'work_place' not in st.session_state:
                    st.session_state['work_place'] = ""
                st.session_state['work_place'] = st.text_area('근무지', value=st.session_state['work_place'])

            with col2:
                custom_css = """
                        <style>
                        .small-text {
                            font-size: 12px; /* 글자 크기 조정 */
                            white-space: nowrap; /* 줄바꿈 방지 */
                            color: #666666; /* 필요시 글자 색상 변경 */
                        }
                        </style>
                        """

                # CSS 적용
                st.markdown(custom_css, unsafe_allow_html=True)

                # 텍스트 출력
                st.markdown('<p class="small-text">· 연봉정보는 통계 자료로만 쓰이며 절대 공개되지 않습니다.</p>', unsafe_allow_html=True)

                col3, col4, col5 = st.columns([2, 0.2, 2])
                with col3:
                    if 'salary_min' not in st.session_state:
                        st.session_state['salary_min'] = 0
                    st.session_state['salary_min'] = st.number_input('최소 연봉 (만원)', min_value=0, max_value=10000, step=10,
                                                                     value=st.session_state['salary_min'])

                with col4:
                    st.write("~")  # 중간에 '~' 기호 표시

                with col5:
                    if 'salary_max' not in st.session_state:
                        st.session_state['salary_max'] = 0
                    st.session_state['salary_max'] = st.number_input('최대 연봉 (만원)', min_value=0, max_value=10000, step=10,
                                                                     value=st.session_state['salary_max'])

            col1, col2 = st.columns(2)
            with col1:
                if 'experience' not in st.session_state:
                    st.session_state['experience'] = "신입"
                st.session_state['experience'] = st.radio("경력", options=["신입", "경력"], index=["신입", "경력"].index(st.session_state['experience']),  horizontal=True)

            with col2:
                if st.session_state['experience'] == "경력":
                    col3, col4, col5 = st.columns([2, 0.2, 2])
                    with col3:
                        if 'year_of_experience_min' not in st.session_state:
                            st.session_state['year_of_experience_min'] = 0
                        st.session_state['year_of_experience_min'] = st.number_input('최소 경력 (년)', min_value=0, max_value=35,
                                                                                     step=1, value=st.session_state['year_of_experience_min'])

                    with col4:
                        st.write("~")  # 중간에 '~' 기호 표시

                    with col5:
                        if 'year_of_experience_max' not in st.session_state:
                            st.session_state['year_of_experience_max'] = 0
                        st.session_state['year_of_experience_max'] = st.number_input('최대 경력 (년)', min_value=0, max_value=35,
                                                                                     step=1, value=st.session_state['year_of_experience_max'])
                    st.write(
                        f"경력: {st.session_state['year_of_experience_min']}년 이상 {st.session_state['year_of_experience_max']}년 이하")

            col1, col2 = st.columns(2)
            with col1:
                if 'date_of_publication' not in st.session_state:
                    st.session_state['date_of_publication'] = "바로 게시"
                st.session_state['date_of_publication'] = st.radio("게시일", options=["바로 게시", "직접 설정"], index=["바로 게시", "직접 설정"].index(st.session_state['date_of_publication']), horizontal=True)

            with col2:
                # 경력 연수 선택 (만약 경력을 선택한 경우만)
                if st.session_state['date_of_publication'] == "직접 설정":
                    date = st.date_input("게시일 입력")

            col1, col2 = st.columns(2)
            with col1:
                if 'Deadline' not in st.session_state:
                    st.session_state['Deadline'] = "상시"
                st.session_state['Deadline'] = st.radio("마감일", options=["상시", "직접 설정"], index=["상시", "직접 설정"].index(st.session_state['Deadline']), horizontal=True)

            with col2:
                # 경력 연수 선택 (만약 경력을 선택한 경우만)
                if st.session_state['Deadline'] == "직접 설정":
                    if 'deadline_date' not in st.session_state:
                        st.session_state['deadline_date'] = datetime.now().date()
                    st.session_state['deadline_date'] = st.date_input("마감일 입력", value=st.session_state['deadline_date'])




### 서비스 기획자 케이스
elif st.session_state['business_registration_number'] == "222-22-22222":

    # 키워드 생성이 활성화된 경우에만 키워드 버튼 표시
    if st.session_state['keyword_generation']:
        st.subheader("네오텍 솔루션")
        st.text_area("회사 소개", st.session_state['neotech'], height=200)
        st.subheader("공고 기반 키워드 선택")

        col1, col2, col3, col4, col5 = st.columns(5)
        # 각 키워드 선택 상태를 체크박스로 표시
        with col1:
            st.session_state['keywords'][0] = st.checkbox('인공지능 서비스 기획', value=st.session_state['keywords'][0], key='kw1')
            if st.session_state['keywords'][0]:
                st.session_state['keywords'][0] = "인공지능 서비스 기획"
        with col2:
            st.session_state['keywords'][1] = st.checkbox('IOT 우대', value=st.session_state['keywords'][1], key='kw2')
            if st.session_state['keywords'][1]:
                st.session_state['keywords'][1] = "IOT 우대"
        with col3:
            st.session_state['keywords'][2] = st.checkbox('경력 3~5년', value=st.session_state['keywords'][2], key='kw3')
            if st.session_state['keywords'][2]:
                st.session_state['keywords'][2] = "경력 3~5년"
        with col4:
            st.session_state['keywords'][3] = st.checkbox('자율출퇴근제', value=st.session_state['keywords'][3],
                                                          key='kw4')
            if st.session_state['keywords'][3]:
                st.session_state['keywords'][3] = "자율출퇴근제"
        with col5:
            st.session_state['keywords'][4] = st.checkbox('서류 및 2회 면접', value=st.session_state['keywords'][4], key='kw5')
            if st.session_state['keywords'][4]:
                st.session_state['keywords'][4] = "서류 및 2회 면접"

        col1, col2, col3 = st.columns(3)
        with col2:
            # CSS 스타일로 버튼 크기 조절
            st.markdown("""
                <style>
                div.stButton > button {
                    font-size: 100px;
                    padding: 10px 20px;
                    width: 100%; /* 버튼을 가로로 꽉 채움 */
                }
                </style>
                """, unsafe_allow_html=True)

            # 버튼 생성
            if st.button("✨ 공고 생성", key='generate_btn'):
                st.session_state['text'] = True
                st.session_state['company_introduction_text'] = """
            주식회사 네오텍솔루션은 인공지능(AI) 기반의 서비스 기획을 담당할 경력 3~5년의 서비스 기획자를 모집하고 있습니다. 
            이 직무는 AI 기술을 바탕으로 사용자 요구를 분석하고, 이를 반영한 서비스 구조 설계 및 기능 정의를 통해 고객 경험을 최적화하는 역할을 수행합니다. 
            서비스 기획자는 서비스 출시와 운영 과정에서 발생하는 문제를 해결하고, 다양한 이해관계자들과의 협업을 통해 프로젝트를 성공적으로 이끌어 나가게 됩니다. 
            또한, 시장 조사 및 최신 기술 트렌드를 반영한 새로운 서비스 아이디어를 제안하며, IoT(사물인터넷) 분야에 대한 이해도가 있으면 우대됩니다. 
            특히 UX/UI 설계 경험이나 데이터 분석 도구를 활용한 서비스 최적화 능력이 있는 분을 환영합니다. 
            자율출퇴근제, 건강 검진 지원, 자기 개발 지원 등 직원 복지와 유연한 근무 환경을 제공하여 창의적이고 자율적인 업무 수행이 가능합니다."""

                st.session_state['major_task_text'] = """
            * 인공지능 기반 서비스의 기획 및 사용자 요구사항 분석
            * 고객 경험을 바탕으로 한 서비스 구조 설계 및 기능 정의
            * 서비스 출시 및 운영 과정에서의 문제 해결 및 최적화
            * 다양한 이해관계자(개발, 디자인, 마케팅 등)와의 협업을 통한 프로젝트 추진
            * 시장 조사 및 트렌드 분석을 바탕으로 한 새로운 서비스 아이디어 제안"""

                st.session_state['qualification_requirements_text'] = """
            * IOT(사물인터넷) 분야에 대한 이해도 및 관련 경험
            * UX/UI 설계에 대한 지식 및 경험
            * 데이터 분석 도구 활용 능력 (Google Analytics, Tableau 등)
            * 스타트업 혹은 IT 서비스 분야에서의 프로젝트 리딩 경험
"""

                st.session_state['benefits_and_welfare_text'] = """
            * 자율출퇴근제: 개인의 업무 스타일에 맞춘 유연한 근무 시간 제공
            * 건강 검진 지원: 직원의 건강을 위한 연간 종합 검진 비용 전액 지원
            * 자기 개발 지원: 세미나, 온라인 강의 등 학습을 위한 비용 지원
            * 유연한 휴가 제도: 충분한 연차와 자유로운 휴가 사용 """

                st.session_state['recruitment_text'] = """
            * 서류 전형: 제출된 이력서 및 포트폴리오를 기반으로 한 서류 평가
            * 1차 면접: 직무 및 인성 면접
            * 2차 면접: 기술 심층 면접 및 실무진 인터뷰
            * 최종 합격: 조건 협의 후 입사
"""

                st.session_state['skill_text'] = """
            * 기획 도구: Jira, Confluence, Notion 등 프로젝트 관리 및 협업 도구
            * 데이터 분석 도구: Google Analytics, Tableau, Excel
            * 협업 도구: Slack, Figma, Zeplin 등 """

    if st.session_state['text']:
        container1 = st.container(border=True)

        with container1:
            # 회사/직무 소개 섹션
            st.subheader("직무 소개")
            st.session_state['company_introduction_text'] = st.text_area(
                '직무 소개', value=st.session_state['company_introduction_text'], height=250,
                label_visibility='collapsed')

            col1, col2, col3 = st.columns([10, 2.8, 2])

            # 회사/직무 소개 전체 삭제 버튼을 누른 경우 텍스트를 삭제
            with col2:
                if st.button("🗑️ 전체 삭제", key='delete_company_intro'):
                    st.session_state['company_introduction_text'] = ""  # 텍스트 상자 내용을 빈 문자열로 설정
                    st.rerun()

            with col3:
                # 복사 버튼을 누른 경우, 복사 알림 메시지 출력
                if st.button("📄 복사", key='copy_company_intro'):
                    pyperclip.copy(st.session_state['company_introduction_text'])  # 텍스트 복사

            # 주요 업무 섹션
            st.subheader("주요 업무")
            st.session_state['major_task_text'] = st.text_area(
                '주요 업무', value=st.session_state['major_task_text'], height=180, label_visibility='collapsed'
            )

            col1, col2, col3 = st.columns([10, 2.8, 2])

            # 주요 업무 전체 삭제 버튼을 누른 경우 텍스트를 삭제
            with col2:
                if st.button("🗑️ 전체 삭제", key='delete_major_tasks'):
                    st.session_state['major_task_text'] = ""  # 텍스트 상자 내용을 빈 문자열로 설정
                    st.rerun()

            with col3:
                # 복사 버튼을 누른 경우, 복사 알림 메시지 출력
                if st.button("📄 복사", key='copy_major_tasks'):
                    pyperclip.copy(st.session_state['major_task_text'])  # 텍스트 복사

            # 우대사항 섹션
            st.subheader("우대사항")
            st.session_state['qualification_requirements_text'] = st.text_area(
                '우대사항', value=st.session_state['qualification_requirements_text'], height=180,
                label_visibility='collapsed'
            )

            col1, col2, col3 = st.columns([10, 2.8, 2])

            # 우대사항 전체 삭제 버튼을 누른 경우 텍스트를 삭제
            with col2:
                if st.button("🗑️ 전체 삭제", key='delete_qualification_requirements'):
                    st.session_state['qualification_requirements_text'] = ""  # 텍스트 상자 내용을 빈 문자열로 설정
                    st.rerun()

            with col3:
                # 복사 버튼을 누른 경우, 복사 알림 메시지 출력
                if st.button("📄 복사", key='copy_qualification_requirements'):
                    pyperclip.copy(st.session_state['qualification_requirements_text'])  # 텍스트 복사

            # 혜택 및 복지 섹션
            st.subheader("혜택 및 복지")
            st.session_state['benefits_and_welfare_text'] = st.text_area(
                '혜택 및 복지', value=st.session_state['benefits_and_welfare_text'], height=160, label_visibility='collapsed'
            )

            col1, col2, col3 = st.columns([10, 2.8, 2])

            # 우대사항 전체 삭제 버튼을 누른 경우 텍스트를 삭제
            with col2:
                if st.button("🗑️ 전체 삭제", key='delete_benefits_and_welfare_text'):
                    st.session_state['benefits_and_welfare_text'] = ""  # 텍스트 상자 내용을 빈 문자열로 설정
                    st.rerun()

            with col3:
                # 복사 버튼을 누른 경우, 복사 알림 메시지 출력
                if st.button("📄 복사", key='copy_benefits_and_welfare_text'):
                    pyperclip.copy(st.session_state['benefits_and_welfare_text'])  # 텍스트 복사

            # 채용 전형 섹션
            st.subheader("채용 전형")
            st.session_state['recruitment_text'] = st.text_area(
                '채용 전형', value=st.session_state['recruitment_text'], height=160, label_visibility='collapsed'
            )

            col1, col2, col3 = st.columns([10, 2.8, 2])

            # 우대사항 전체 삭제 버튼을 누른 경우 텍스트를 삭제
            with col2:
                if st.button("🗑️ 전체 삭제", key='delete_recruitment_text'):
                    st.session_state['recruitment_text'] = ""  # 텍스트 상자 내용을 빈 문자열로 설정
                    st.rerun()

            with col3:
                # 복사 버튼을 누른 경우, 복사 알림 메시지 출력
                if st.button("📄 복사", key='copy_recruitment_text'):
                    pyperclip.copy(st.session_state['recruitment_text'])  # 텍스트 복사

            # 채용 전형 섹션
            st.subheader("기술 스택")
            st.session_state['skill_text'] = st.text_area(
                '기술 스택', value=st.session_state['skill_text'], height=140, label_visibility='collapsed'
            )

            col1, col2, col3 = st.columns([10, 2.8, 2])

            # 우대사항 전체 삭제 버튼을 누른 경우 텍스트를 삭제
            with col2:
                if st.button("🗑️ 전체 삭제", key='delete_skill_text'):
                    st.session_state['skill_text'] = ""  # 텍스트 상자 내용을 빈 문자열로 설정
                    st.rerun()

            with col3:
                # 복사 버튼을 누른 경우, 복사 알림 메시지 출력
                if st.button("📄 복사", key='copy_skill_text'):
                    pyperclip.copy(st.session_state['skill_text'])  # 텍스트 복사

        container2 = st.container(border=True)

        with container2:
            # 직군/직무 선택
            st.subheader("직군/직무")

            # 직군 선택 (왼쪽 셀렉트박스)
            if 'job_category' not in st.session_state:
                st.session_state['job_category'] = ""
            st.session_state['job_category'] = st.selectbox("직군",
                                                            options=["경영·비즈니스", "개발", "디자인", "마케팅", "인사", "운영", "교육"])

            # 직무 선택 (오른쪽 셀렉트박스)
            if 'job_role' not in st.session_state:
                st.session_state['job_role'] = ""
            st.session_state['job_role'] = st.selectbox("직무",
                                                        options=["서비스 기획자", "데이터 분석가", "디자이너", "백엔드 개발자", "프론트엔드 개발자",
                                                                 "인공지능 강사"])

            col1, col2 = st.columns(2)
            with col1:
                if 'work_place' not in st.session_state:
                    st.session_state['work_place'] = ""
                st.session_state['work_place'] = st.text_area('근무지', value=st.session_state['work_place'])

            with col2:
                custom_css = """
                        <style>
                        .small-text {
                            font-size: 12px; /* 글자 크기 조정 */
                            white-space: nowrap; /* 줄바꿈 방지 */
                            color: #666666; /* 필요시 글자 색상 변경 */
                        }
                        </style>
                        """

                # CSS 적용
                st.markdown(custom_css, unsafe_allow_html=True)

                # 텍스트 출력
                st.markdown('<p class="small-text">· 연봉정보는 통계 자료로만 쓰이며 절대 공개되지 않습니다.</p>', unsafe_allow_html=True)

                col3, col4, col5 = st.columns([2, 0.2, 2])
                with col3:
                    if 'salary_min' not in st.session_state:
                        st.session_state['salary_min'] = 0
                    st.session_state['salary_min'] = st.number_input('최소 연봉 (만원)', min_value=0, max_value=10000,
                                                                     step=10,
                                                                     value=st.session_state['salary_min'])

                with col4:
                    st.write("~")  # 중간에 '~' 기호 표시

                with col5:
                    if 'salary_max' not in st.session_state:
                        st.session_state['salary_max'] = 0
                    st.session_state['salary_max'] = st.number_input('최대 연봉 (만원)', min_value=0, max_value=10000,
                                                                     step=10,
                                                                     value=st.session_state['salary_max'])

            col1, col2 = st.columns(2)
            with col1:
                if 'experience' not in st.session_state:
                    st.session_state['experience'] = "신입"
                st.session_state['experience'] = st.radio("경력", options=["신입", "경력"],
                                                          index=["신입", "경력"].index(st.session_state['experience']),
                                                          horizontal=True)

            with col2:
                if st.session_state['experience'] == "경력":
                    col3, col4, col5 = st.columns([2, 0.2, 2])
                    with col3:
                        if 'year_of_experience_min' not in st.session_state:
                            st.session_state['year_of_experience_min'] = 0
                        st.session_state['year_of_experience_min'] = st.number_input('최소 경력 (년)', min_value=0,
                                                                                     max_value=35,
                                                                                     step=1, value=st.session_state[
                                'year_of_experience_min'])

                    with col4:
                        st.write("~")  # 중간에 '~' 기호 표시

                    with col5:
                        if 'year_of_experience_max' not in st.session_state:
                            st.session_state['year_of_experience_max'] = 0
                        st.session_state['year_of_experience_max'] = st.number_input('최대 경력 (년)', min_value=0,
                                                                                     max_value=35,
                                                                                     step=1, value=st.session_state[
                                'year_of_experience_max'])
                    st.write(
                        f"경력: {st.session_state['year_of_experience_min']}년 이상 {st.session_state['year_of_experience_max']}년 이하")

            col1, col2 = st.columns(2)
            with col1:
                if 'date_of_publication' not in st.session_state:
                    st.session_state['date_of_publication'] = "바로 게시"
                st.session_state['date_of_publication'] = st.radio("게시일", options=["바로 게시", "직접 설정"],
                                                                   index=["바로 게시", "직접 설정"].index(
                                                                       st.session_state['date_of_publication']),
                                                                   horizontal=True)

            with col2:
                # 경력 연수 선택 (만약 경력을 선택한 경우만)
                if st.session_state['date_of_publication'] == "직접 설정":
                    date = st.date_input("게시일 입력")

            col1, col2 = st.columns(2)
            with col1:
                if 'Deadline' not in st.session_state:
                    st.session_state['Deadline'] = "상시"
                st.session_state['Deadline'] = st.radio("마감일", options=["상시", "직접 설정"],
                                                        index=["상시", "직접 설정"].index(st.session_state['Deadline']),
                                                        horizontal=True)

            with col2:
                # 경력 연수 선택 (만약 경력을 선택한 경우만)
                if st.session_state['Deadline'] == "직접 설정":
                    if 'deadline_date' not in st.session_state:
                        st.session_state['deadline_date'] = datetime.now().date()
                    st.session_state['deadline_date'] = st.date_input("마감일 입력", value=st.session_state['deadline_date'])

### 친환경 제품 개발자
elif st.session_state['business_registration_number'] == "333-33-33333":
    # 키워드 생성이 활성화된 경우에만 키워드 버튼 표시
    if st.session_state['keyword_generation']:
        st.subheader("주식회사 그린메이커스")
        st.text_area("회사 소개", st.session_state['green'], height=200)
        st.subheader("공고 기반 키워드 선택")
        col1, col2, col3, col4, col5 = st.columns(5)
        # 각 키워드 선택 상태를 체크박스로 표시
        with col1:
            st.session_state['keywords'][0] = st.checkbox('친환경 제품 개발 ', value=st.session_state['keywords'][0], key='kw1')
            if st.session_state['keywords'][0]:
                st.session_state['keywords'][0] = "친환경 제품 개발"
        with col2:
            st.session_state['keywords'][1] = st.checkbox('에너지 절감 기술', value=st.session_state['keywords'][1], key='kw2')
            if st.session_state['keywords'][1]:
                st.session_state['keywords'][1] = "에너지 절감 기술"
        with col3:
            st.session_state['keywords'][2] = st.checkbox('경력 2~3년', value=st.session_state['keywords'][2], key='kw3')
            if st.session_state['keywords'][2]:
                st.session_state['keywords'][2] = "경력 2~3년"
        with col4:
            st.session_state['keywords'][3] = st.checkbox('자율출퇴근제', value=st.session_state['keywords'][3],
                                                          key='kw4')
            if st.session_state['keywords'][3]:
                st.session_state['keywords'][3] = "자율출퇴근제"
        with col5:
            st.session_state['keywords'][4] = st.checkbox('교육 및 세미나 지원', value=st.session_state['keywords'][4], key='kw5')
            if st.session_state['keywords'][4]:
                st.session_state['keywords'][4] = "교육 및 세미나 지원"

        col1, col2, col3 = st.columns(3)
        with col2:
            # CSS 스타일로 버튼 크기 조절
            st.markdown("""
                <style>
                div.stButton > button {
                    font-size: 100px;
                    padding: 10px 20px;
                    width: 100%; /* 버튼을 가로로 꽉 채움 */
                }
                </style>
                """, unsafe_allow_html=True)

            # 버튼 생성
            if st.button("✨ 공고 생성", key='generate_btn'):
                st.session_state['text'] = True
                st.session_state['company_introduction_text'] = """
            주식회사 그린메이커스는 지속 가능한 제품 개발을 통해 친환경 솔루션을 제공하는 혁신적인 제조업체로, 경력 2~3년의 친환경 제품 개발 전문가를 모집합니다. 
            이 직무는 에너지 절감 및 자원 효율성을 극대화할 수 있는 기술을 연구하고 이를 제품 설계에 반영하는 것을 목표로 합니다. 
            친환경 제품의 설계부터 제조 공정 개선에 이르기까지 전 과정에 걸쳐 중요한 역할을 하며, 최신 친환경 기술 트렌드 도입을 통해 제품 성능을 지속적으로 향상시키는 책임을 맡게 됩니다. 
            주요 업무에는 지속 가능한 제품 개발, 에너지 절감 기술 연구 및 제조 공정 최적화가 포함됩니다. 
            우대 사항으로는 친환경 제품 개발 경험, CAD 및 3D 모델링 툴 사용 능력, 프로젝트 관리 경험 등이 있으며, 다양한 산업에서의 경험을 가진 지원자를 선호합니다. 
            자율출퇴근제와 같은 유연한 근무 환경, 건강 검진 및 의료 지원, 교육 및 세미나 참여 기회 등 다양한 혜택을 통해 직원들의 복지를 보장합니다."""

                st.session_state['major_task_text'] = """
            * 지속 가능한 친환경 제품 설계 및 개발
            * 에너지 절감 및 자원 효율성을 극대화하는 기술 연구 및 적용
            * 제조 공정 개선을 위한 기술 솔루션 제안 및 실행
            * 제품의 품질 관리 및 성능 향상 방안 개발
            * 최신 친환경 기술 트렌드 조사 및 도입"""

                st.session_state['qualification_requirements_text'] = """
            * 친환경 제품 개발 또는 에너지 절감 기술 관련 경험
            * 지속 가능한 자원 관리 및 최적화 경험
            * 다양한 산업 분야에서의 제품 개발 및 프로젝트 관리 경험
            * CAD 및 3D 모델링 툴 사용 경험

"""
                st.session_state['benefits_and_welfare_text'] = """
            * 자율출퇴근제: 업무 시간에 대한 유연성을 제공하여 개인의 업무 스타일에 맞춘 근무 가능
            * 건강 검진 및 의료 지원: 직원의 건강을 위한 연간 종합 검진과 의료 지원
            * 교육 및 세미나 지원: 관련 분야의 최신 트렌드와 기술을 익히기 위한 교육 및 세미나 참여 지원
            * 자기 개발 지원: 지속적인 학습과 성장을 위한 자기 개발 비용 지원
"""

                st.session_state['recruitment_text'] = """
            * 서류 전형: 지원서 및 자기소개서 기반 평가
            * 1차 면접: 직무 및 인성 면접
            * 2차 면접: 심층 면접 및 실무진 인터뷰
            * 최종 합격: 조건 협의 후 입사


"""
                st.session_state['skill_text'] = """
            * 설계 도구: AutoCAD, SolidWorks 등
            * 데이터 분석 도구: Excel, MATLAB
            * 프로젝트 관리 도구: Jira, Trello
            * 기술 트렌드: 지속 가능한 기술, 에너지 절감 솔루션, 친환경 자원 관리 기술
 """

    if st.session_state['text']:
        container1 = st.container(border=True)

        with container1:
            # 회사/직무 소개 섹션
            st.subheader("직무 소개")
            st.session_state['company_introduction_text'] = st.text_area(
                '직무 소개', value=st.session_state['company_introduction_text'], height=250,
                label_visibility='collapsed')

            col1, col2, col3 = st.columns([10, 2.8, 2])

            # 회사/직무 소개 전체 삭제 버튼을 누른 경우 텍스트를 삭제
            with col2:
                if st.button("🗑️ 전체 삭제", key='delete_company_intro'):
                    st.session_state['company_introduction_text'] = ""  # 텍스트 상자 내용을 빈 문자열로 설정
                    st.rerun()

            with col3:
                # 복사 버튼을 누른 경우, 복사 알림 메시지 출력
                if st.button("📄 복사", key='copy_company_intro'):
                    pyperclip.copy(st.session_state['company_introduction_text'])  # 텍스트 복사

            # 주요 업무 섹션
            st.subheader("주요 업무")
            st.session_state['major_task_text'] = st.text_area(
                '주요 업무', value=st.session_state['major_task_text'], height=180, label_visibility='collapsed'
            )

            col1, col2, col3 = st.columns([10, 2.8, 2])

            # 주요 업무 전체 삭제 버튼을 누른 경우 텍스트를 삭제
            with col2:
                if st.button("🗑️ 전체 삭제", key='delete_major_tasks'):
                    st.session_state['major_task_text'] = ""  # 텍스트 상자 내용을 빈 문자열로 설정
                    st.rerun()

            with col3:
                # 복사 버튼을 누른 경우, 복사 알림 메시지 출력
                if st.button("📄 복사", key='copy_major_tasks'):
                    pyperclip.copy(st.session_state['major_task_text'])  # 텍스트 복사

            # 우대사항 섹션
            st.subheader("우대사항")
            st.session_state['qualification_requirements_text'] = st.text_area(
                '우대사항', value=st.session_state['qualification_requirements_text'], height=180,
                label_visibility='collapsed'
            )

            col1, col2, col3 = st.columns([10, 2.8, 2])

            # 우대사항 전체 삭제 버튼을 누른 경우 텍스트를 삭제
            with col2:
                if st.button("🗑️ 전체 삭제", key='delete_qualification_requirements'):
                    st.session_state['qualification_requirements_text'] = ""  # 텍스트 상자 내용을 빈 문자열로 설정
                    st.rerun()

            with col3:
                # 복사 버튼을 누른 경우, 복사 알림 메시지 출력
                if st.button("📄 복사", key='copy_qualification_requirements'):
                    pyperclip.copy(st.session_state['qualification_requirements_text'])  # 텍스트 복사

            # 혜택 및 복지 섹션
            st.subheader("혜택 및 복지")
            st.session_state['benefits_and_welfare_text'] = st.text_area(
                '혜택 및 복지', value=st.session_state['benefits_and_welfare_text'], height=160, label_visibility='collapsed'
            )

            col1, col2, col3 = st.columns([10, 2.8, 2])

            # 우대사항 전체 삭제 버튼을 누른 경우 텍스트를 삭제
            with col2:
                if st.button("🗑️ 전체 삭제", key='delete_benefits_and_welfare_text'):
                    st.session_state['benefits_and_welfare_text'] = ""  # 텍스트 상자 내용을 빈 문자열로 설정
                    st.rerun()

            with col3:
                # 복사 버튼을 누른 경우, 복사 알림 메시지 출력
                if st.button("📄 복사", key='copy_benefits_and_welfare_text'):
                    pyperclip.copy(st.session_state['benefits_and_welfare_text'])  # 텍스트 복사

            # 채용 전형 섹션
            st.subheader("채용 전형")
            st.session_state['recruitment_text'] = st.text_area(
                '채용 전형', value=st.session_state['recruitment_text'], height=160, label_visibility='collapsed'
            )

            col1, col2, col3 = st.columns([10, 2.8, 2])

            # 우대사항 전체 삭제 버튼을 누른 경우 텍스트를 삭제
            with col2:
                if st.button("🗑️ 전체 삭제", key='delete_recruitment_text'):
                    st.session_state['recruitment_text'] = ""  # 텍스트 상자 내용을 빈 문자열로 설정
                    st.rerun()

            with col3:
                # 복사 버튼을 누른 경우, 복사 알림 메시지 출력
                if st.button("📄 복사", key='copy_recruitment_text'):
                    pyperclip.copy(st.session_state['recruitment_text'])  # 텍스트 복사

            # 채용 전형 섹션
            st.subheader("기술 스택")
            st.session_state['skill_text'] = st.text_area(
                '기술 스택', value=st.session_state['skill_text'], height=160, label_visibility='collapsed'
            )

            col1, col2, col3 = st.columns([10, 2.8, 2])

            # 우대사항 전체 삭제 버튼을 누른 경우 텍스트를 삭제
            with col2:
                if st.button("🗑️ 전체 삭제", key='delete_skill_text'):
                    st.session_state['skill_text'] = ""  # 텍스트 상자 내용을 빈 문자열로 설정
                    st.rerun()

            with col3:
                # 복사 버튼을 누른 경우, 복사 알림 메시지 출력
                if st.button("📄 복사", key='copy_skill_text'):
                    pyperclip.copy(st.session_state['skill_text'])  # 텍스트 복사

        container2 = st.container(border=True)

        with container2:
            # 직군/직무 선택
            st.subheader("직군/직무")

            # 직군 선택 (왼쪽 셀렉트박스)
            if 'job_category' not in st.session_state:
                st.session_state['job_category'] = ""
            st.session_state['job_category'] = st.selectbox("직군",
                                                            options=["경영·비즈니스", "개발", "디자인", "마케팅", "인사", "운영", "교육"])

            # 직무 선택 (오른쪽 셀렉트박스)
            if 'job_role' not in st.session_state:
                st.session_state['job_role'] = ""
            st.session_state['job_role'] = st.selectbox("직무",
                                                        options=["서비스 기획자", "데이터 분석가", "디자이너", "백엔드 개발자", "프론트엔드 개발자",
                                                                 "인공지능 강사"])

            col1, col2 = st.columns(2)
            with col1:
                if 'work_place' not in st.session_state:
                    st.session_state['work_place'] = ""
                st.session_state['work_place'] = st.text_area('근무지', value=st.session_state['work_place'])

            with col2:
                custom_css = """
                        <style>
                        .small-text {
                            font-size: 12px; /* 글자 크기 조정 */
                            white-space: nowrap; /* 줄바꿈 방지 */
                            color: #666666; /* 필요시 글자 색상 변경 */
                        }
                        </style>
                        """

                # CSS 적용
                st.markdown(custom_css, unsafe_allow_html=True)

                # 텍스트 출력
                st.markdown('<p class="small-text">· 연봉정보는 통계 자료로만 쓰이며 절대 공개되지 않습니다.</p>', unsafe_allow_html=True)

                col3, col4, col5 = st.columns([2, 0.2, 2])
                with col3:
                    if 'salary_min' not in st.session_state:
                        st.session_state['salary_min'] = 0
                    st.session_state['salary_min'] = st.number_input('최소 연봉 (만원)', min_value=0, max_value=10000,
                                                                     step=10,
                                                                     value=st.session_state['salary_min'])

                with col4:
                    st.write("~")  # 중간에 '~' 기호 표시

                with col5:
                    if 'salary_max' not in st.session_state:
                        st.session_state['salary_max'] = 0
                    st.session_state['salary_max'] = st.number_input('최대 연봉 (만원)', min_value=0, max_value=10000,
                                                                     step=10,
                                                                     value=st.session_state['salary_max'])

            col1, col2 = st.columns(2)
            with col1:
                if 'experience' not in st.session_state:
                    st.session_state['experience'] = "신입"
                st.session_state['experience'] = st.radio("경력", options=["신입", "경력"],
                                                          index=["신입", "경력"].index(st.session_state['experience']),
                                                          horizontal=True)

            with col2:
                if st.session_state['experience'] == "경력":
                    col3, col4, col5 = st.columns([2, 0.2, 2])
                    with col3:
                        if 'year_of_experience_min' not in st.session_state:
                            st.session_state['year_of_experience_min'] = 0
                        st.session_state['year_of_experience_min'] = st.number_input('최소 경력 (년)', min_value=0,
                                                                                     max_value=35,
                                                                                     step=1, value=st.session_state[
                                'year_of_experience_min'])

                    with col4:
                        st.write("~")  # 중간에 '~' 기호 표시

                    with col5:
                        if 'year_of_experience_max' not in st.session_state:
                            st.session_state['year_of_experience_max'] = 0
                        st.session_state['year_of_experience_max'] = st.number_input('최대 경력 (년)', min_value=0,
                                                                                     max_value=35,
                                                                                     step=1, value=st.session_state[
                                'year_of_experience_max'])
                    st.write(
                        f"경력: {st.session_state['year_of_experience_min']}년 이상 {st.session_state['year_of_experience_max']}년 이하")

            col1, col2 = st.columns(2)
            with col1:
                if 'date_of_publication' not in st.session_state:
                    st.session_state['date_of_publication'] = "바로 게시"
                st.session_state['date_of_publication'] = st.radio("게시일", options=["바로 게시", "직접 설정"],
                                                                   index=["바로 게시", "직접 설정"].index(
                                                                       st.session_state['date_of_publication']), horizontal=True)

            with col2:
                # 경력 연수 선택 (만약 경력을 선택한 경우만)
                if st.session_state['date_of_publication'] == "직접 설정":
                    date = st.date_input("게시일 입력")

            col1, col2 = st.columns(2)
            with col1:
                if 'Deadline' not in st.session_state:
                    st.session_state['Deadline'] = "상시"
                st.session_state['Deadline'] = st.radio("마감일", options=["상시", "직접 설정"],
                                                        index=["상시", "직접 설정"].index(st.session_state['Deadline']),
                                                        horizontal=True)

            with col2:
                # 경력 연수 선택 (만약 경력을 선택한 경우만)
                if st.session_state['Deadline'] == "직접 설정":
                    if 'deadline_date' not in st.session_state:
                        st.session_state['deadline_date'] = datetime.now().date()
                    st.session_state['deadline_date'] = st.date_input("마감일 입력", value=st.session_state['deadline_date'])