# app.py

import warnings
import streamlit as st
from streamlit_option_menu import option_menu
import base64
from streamlit_lottie import st_lottie
import json

warnings.simplefilter(action="ignore", category=FutureWarning)

# Must be the first Streamlit command
st.set_page_config(page_title="Personalsite", layout="wide")

def add_top_banner(image_path: str, banner_height_px: int = 150):
    with open(image_path, "rb") as f:
        image_bytes = f.read()
    b64_encoded = base64.b64encode(image_bytes).decode()

    banner_html = f"""
    <div style="width:100%; overflow:hidden; margin-bottom:20px;">
      <img 
        src="data:image/png;base64,{b64_encoded}" 
        style="width:100%; height:auto; display:block;"
        alt="top banner"
      >
    </div>
    """
    st.markdown(banner_html, unsafe_allow_html=True)

# 页面导入
from page_content.home import home_page
from page_content.education import education_page
from page_content.experience import experience_page
from page_content.resume import resume_page
from page_content.contact import contact_page

from components.footer import display_footer
from components.styles import load_css

class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, func, icon):
        self.apps.append({"title": title, "function": func, "icon": icon})

    def run(self):
        load_css()
        add_top_banner("static/images/image_2.jpg", banner_height_px=150)

        with st.sidebar:
            st.markdown("## Main Menu")
            selected = option_menu(
                menu_title=None,
                options=[app["title"] for app in self.apps],
                icons=[app["icon"] for app in self.apps],
                menu_icon="cast",
                default_index=0,
                orientation="vertical",
                styles={
                    "container": {
                        "padding": "4px",
                        "background-color": "#fafafa",
                    },
                    "icon": {
                        "font-size": "20px",
                        "color": "#0055aa",
                    },
                    "nav-link": {
                        "font-size": "16px",
                        "text-align": "left",
                        "margin": "6px 0",
                        "--hover-color": "#e8f0fe",
                    },
                    "nav-link-selected": {
                        "background": "linear-gradient(90deg, #0055aa, #00aaff)",
                        "color": "white",
                        "border-radius": "8px",
                    },
                },
            )
            st.markdown("---")

        for app in self.apps:
            if app["title"] == selected:
                app["function"]()

        display_footer()

# 主题切换逻辑（可选）
if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = False

if st.button("🌙 Toggle Dark Mode"):
    st.session_state.dark_mode = not st.session_state.dark_mode

if st.session_state.dark_mode:
    st.markdown("""
    <style>
    body, .stApp {
        background-color: #111 !important;
        color: #ffffff !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 注册页面
app = MultiApp()
app.add_app("Home", home_page, "house")
app.add_app("Education", education_page, "book")
app.add_app("Experience", experience_page, "briefcase")
# app.add_app("Resume", resume_page, "file-earmark-text")
app.add_app("Contact", contact_page, "envelope")
app.run()
