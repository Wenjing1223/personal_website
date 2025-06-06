import os
import base64
import streamlit as st

def education_page():
    st.markdown("## Education")

    # 加载 CUHK logo
    cuhk_logo_path = os.path.join("static", "images", "CUHK.png")
    if os.path.exists(cuhk_logo_path):
        with open(cuhk_logo_path, "rb") as f:
            cuhk_logo_b64 = base64.b64encode(f.read()).decode()
        cuhk_logo_html = f"""<img src="data:image/png;base64,{cuhk_logo_b64}" 
             width="28" style="vertical-align: middle; margin-right: 8px;">"""
    else:
        cuhk_logo_html = ""
    
    unsw_logo_path = os.path.join("static", "images", "UNSW.png")
    if os.path.exists(unsw_logo_path):
        with open(unsw_logo_path, "rb") as f:
            unsw_logo_b64 = base64.b64encode(f.read()).decode()
        unsw_logo_html = f"""<img src="data:image/png;base64,{unsw_logo_b64}" 
             width="28" style="vertical-align: middle; margin-right: 8px;">"""
    else:
        unsw_logo_html = ""

    # 使用 st.markdown 插入整段 HTML（必须保证标签不能被换行截断）
    st.markdown(f"""
        <h4>Master of Science in Marketing</h4>
        <p>
            {cuhk_logo_html}
            <strong>Chinese University of Hong Kong</strong> |
            <em>August 2024 - June 2025</em><br>
            GPA: 3.6/4.0<br>
            Relevant Coursework: Advanced Machine Learning, Deep Learning, Natural Language Processing, Data Visualization, Statistical Methods for Data Science, Big Data Analytics, Marketing Analytics, Marketing Research, Marketing Management, Consumer Behavior, Marketing Strategy
        </p>

        <h4>Bachelor of Science in Psychology</h4>
        <p>
            {unsw_logo_html}
            <strong>University of New South Wales</strong> |
            <em>September 2020 - August 2023</em><br>
            GPA: 3.9/4.0<br>
            Graduated with Honors<br>
            Relevant Coursework: Social Psychology, Developmental Psychology, Clinical Psychology, Cognitive Psychology, Physiological Psychology, Research Methods, Statistics, Quantitative Methods, Qualitative Methods, Research Design, Research Proposal
        </p>
    """, unsafe_allow_html=True)

    st.markdown("---")

    
    st.markdown("## Awards")
    
    cert1, cert2, cert3 = st.columns(3)
    
    with cert1:
        st.markdown("""
        ### Second Prize
        **GuangDong, China** | *March 2019*
        
        **34th Guangdong Adolescents Science and Technology Innovation Contest**
        """)
        
    with cert2:
        st.markdown("""
        ### Gold Medal
        **Nuremberg, Germany** | *November 2018*
        
        **International Invention Exhibition**
        """)
        
    
    st.markdown("---")
    
    st.markdown("## Academic Projects")
    
    st.markdown("""
    ### Clinical Psychology: DSM based Diagnosis
    - Refer to the DSM manual for a symptom analysis of a 6-year-old child to provide a proper diagnosis
    - Supplied rational and multifaceted interventions for the diagnosed object, such as behavioral observation and CBT treatment
    - Assessed whether the condition meets the diagnostic criteria
    - Analyzed the advantages and disadvantages of the interventions for the disorder (Distinction grade)
    """)
    
    st.markdown("---") 