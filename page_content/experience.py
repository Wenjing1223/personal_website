import streamlit as st
from components.interactive import display_interactive_chart

def experience_page():
    st.markdown("## Professional Experience")
    
    st.markdown("""
    ### Big Data Marketing Intern
    **Omnicom Media Group** | *December 2024 - March 2025*
    
    - Developed a Xiaohongshu strategy for the Hong Kong market to support its entry
    """)
    
    st.markdown("""
    ### Research Assistant
    **Institute of Psychology, Chinese Academy of Sciences** | *October 2022 - February 2023*
    
    - Assisted professor with research on natural language processing techniques
    - Implemented and evaluated various machine learning algorithms for text classification
    - Co-authored a paper that was accepted at a regional computer science conference
    - Mentored undergraduate students on research methodologies and programming
    """)
    
    st.markdown("""
    ### Clinical psychology Intern
    **1st Affiliated Hospital of Sun Yat-sen University** | *September 2021 - March 2022*
    
    - Conducted psychological assessments and provided interventions for patients with psychological disorders
    - Collaborated with a team of psychologists and psychiatrists to develop treatment plans
    - Participated in clinical research and contributed to the development of new psychological interventions
    - Provided support to the clinical team in the preparation of case reports and clinical trial documentation
    """)
    
    st.markdown("---")
    
    st.markdown("## Professional Skills")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### Technical Skills
        - **Programming Languages:** Python, R
        - **Data Processing:** Pandas, NumPy
        - **Visualization:** Matplotlib
        - **Cloud Platforms:** Google Cloud
        """)
        
    with col2:
        st.markdown("""
        ### Soft Skills
        - **Communication:** Excellent written and verbal communication
        - **Teamwork:** Collaborative team members with experience in flexible working environments
        - **Problem-solving:** Strong analytical and critical thinking abilities
        - **Time Management:** Efficient at prioritizing tasks and meeting deadlines
        - **Leadership:** Experience leading small teams and mentoring junior colleagues
        - **Adaptability:** Quick learner who thrives in dynamic environments
        """)
    
    st.markdown("---") 