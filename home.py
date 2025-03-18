import streamlit as st
from streamlit_option_menu import option_menu
import base64
from streamlit_lottie import st_lottie
import requests
import json
from reume_page import resume
from experience_page import experience
from project_page import projects
from contact_form import contact

# Page setup
st.set_page_config(
    page_title="Ayush",
    page_icon="📋",
    layout="wide",
)

def aboutMe():
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <style>
        .center-text {
        text-align: justify;
        }
        </style>
        <div class="justify-text">
        
        Hello! I’m Ayush Kumar Sahu, a passionate and driven B.Tech Computer Science student specializing in Data Science at SSTC. With a strong foundation in programming and data analysis, I am enthusiastic about building innovative solutions and mentoring aspiring learners.

        I recently completed an internship at BSP SAIL, where I contributed to developing an e-pharmacy and medical appointment website, leveraging MapMyIndia’s API and React to build an interactive framework. Currently, I am interning at The iScale, where I serve as a mentor for Data Analytics students, helping them navigate the world of data-driven insights.

        My toolkit includes Python, React, and Power BI, and I’m always eager to learn and share knowledge. Whether it’s mentoring, solving complex data challenges, or crafting engaging web applications, I thrive on turning ideas into impactful solutions.

        Let’s connect and collaborate on projects that make a difference!
        </div>
        """, unsafe_allow_html=True)

        c1, c2 = st.columns(2)
        c1.markdown("""<a href="https://github.com/ayushkanha" target="_blank" style="text-decoration:none;"><button style="background-color:#6C63FF;color:white;padding:10px 15px;border:none;border-radius:5px;cursor:pointer;">GitHub</button></a>""", unsafe_allow_html=True)
        c2.markdown("""<a href="https://linkedin.com/in/ayush-kumar-sahu-299b8b23b" target="_blank" style="text-decoration:none;"><button style="background-color:#0077B5;color:white;padding:10px 15px;border:none;border-radius:5px;cursor:pointer;">LinkedIn</button></a>""", unsafe_allow_html=True)
    
    path = "Animation_blue_robo.json"
    with open(path, "r") as file:
        url = json.load(file)
    with col2:
        st_lottie(url, height=400, width=400, speed=1, loop=True, quality='high')

def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

logo_base64 = get_base64_image("ayush_pp.jpeg")
logo_html = f"""
    <style>
    .logo-container {{
        display: flex;
        justify-content: center;
        margin-bottom: 20px;
    }}
    .logo {{
        width: 120px;
        height: 120px;
        border-radius: 50%;
        object-fit: cover;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.3);
    }}
    .sidebar-links a:hover {{
        color: #6C63FF;
        font-weight: bold;
    }}
    </style>
    <div class="logo-container">
        <img src="data:image/png;base64,{logo_base64}" class="logo">
    </div>
"""

st.sidebar.markdown(logo_html, unsafe_allow_html=True)
with st.sidebar:
    pages = ["About me", "Resume", "Experience",  "Projects", "Contact"]
    nav_tab_op = option_menu(
        menu_title="Ayush",
        options=pages,
        icons=['person-fill', 'file-text', 'briefcase', 'folder', 'star', 'envelope'],
        menu_icon="cast",
        default_index=0,
    )

if nav_tab_op == "About me":
    aboutMe()
elif nav_tab_op == "Resume":
    resume()
elif nav_tab_op == "Experience":
    experience()
elif nav_tab_op == "Projects":
    projects()
elif nav_tab_op == "Contact":
    contact()
