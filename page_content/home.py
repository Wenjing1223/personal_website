import os
from PIL import Image
import streamlit as st
from streamlit_lottie import st_lottie
import json

def load_lottie_file(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

def home_page():
    left_col, right_col = st.columns(2)

    left_col.markdown(
        """
        <h4>Wenjing Zhang</h4>
        <p>Recent Master's Graduate in Marketing<br>
        Chinese University of Hong Kong<br>
        12 Chak Cheung St., Ma Liu Shui, HKSAR<br>
        <a href="mailto:heyblibiu@163.com">heyblibiu@163.com</a></p>
        """,
        unsafe_allow_html=True
    )

    # add a photo to the right column, aligned right
    image_path = os.path.join("static", "images", "image_1.png")
    if os.path.exists(image_path):
        with open(image_path, "rb") as f:
            data = f.read()
        import base64
        b64 = base64.b64encode(data).decode()
        right_col.markdown(
            f"""
            <div style="text-align: right;">
                <img src="data:image/png;base64,{b64}" width="150">
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        right_col.warning("Profile image not found")

    st.markdown("---")


    st.markdown(
        """
        ### About Me
        I hold a Master’s degree in Marketing from The Chinese University of Hong Kong, where I honed my expertise in statistical analysis, machine learning, and data visualization. Throughout my studies, I tackled multiple real-world data projects—handling data preprocessing, exploratory analysis, and performance evaluation.

        I thrive on turning complex data into actionable insights. As a fast learner and collaborative team player, I bring strong problem-solving skills and a passion for data-driven decision making. I’m eager to apply my abilities and continue growing in a dynamic data science role.
        """
    )

    st.markdown(
        """
        ### Skills
        - **Programming & Scripting:** Python, R  
        - **Data Manipulation:** Pandas, NumPy  
        - **Visualization:** Matplotlib, Seaborn, Tableau, Power BI  
        - **Machine Learning:** Scikit-learn, TensorFlow, Keras  
        - **Databases:** SQL, MongoDB  
        - **Statistics & Analysis:** Hypothesis Testing, Regression Analysis  
        - **Communication:** Technical Writing, Presentations  
        """
    )
    lottie_path = os.path.join("static", "success.json")
    if os.path.exists(lottie_path):
        animation = load_lottie_file(lottie_path)
        st_lottie(animation, speed=1, loop=True, height=250)
    else:
        st.warning("Animation file not found at 'static/success.json'")

    st.markdown("---")

    
    # Interactive component has been moved to the experience page 