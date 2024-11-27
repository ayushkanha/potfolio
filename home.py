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


def gradient(color1, color2, color3, content1, content2):
    st.markdown(f'<h1 style="text-align:center;background-image: linear-gradient(to right,{color1}, {color2});font-size:60px;border-radius:2%;">'
                f'<span style="color:{color3};">{content1}</span><br>'
                f'<span style="color:white;font-size:17px;">{content2}</span></h1>',
                unsafe_allow_html=True)
def aboutMe():
    col1, col2 = st.columns(2)
    full_name = "Ayush Kumar Sahu"
    info = {'Intro': "Data scientist"}

    with col1:
        st.markdown("<h2 style='text-align: center; '>Hello! I'm Ayush 👋</h2>", unsafe_allow_html=True)

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
        c1,c2 =st.columns(2)
        c1.markdown("""**[GitHub](https://github.com/ayushkanha)**""")
        c2.markdown("""**[LinkedIn](https://linkedin.com/in/ayush-kumar-sahu-299b8b23b)** """)
      
    path = "Animation_blue_robo.json"
    with open(path, "r") as file:
        url = json.load(file)
    with col2:

        st_lottie(url,
                  reverse=True,
                  height=400,
                  width=400,
                  speed=1,
                  loop=True,
                  quality='high',
                  )
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Get the base64 string of the image
logo_base64 = get_base64_image("ayush.jpeg")

# Logo styling
logo_html = f"""
    <style>
    .logo-container {{
        display: flex;
        justify-content: center;
        margin-bottom: 20px;
    }}
    .logo {{
        width: 100px;
        height: 100px;
        border-radius: 50%;
        object-fit: cover;
    }}
    </style>
    <div class="logo-container">
        <img src="data:image/png;base64,{logo_base64}" class="logo">
    </div>
"""

# Display logo in the sidebar
st.sidebar.markdown(logo_html, unsafe_allow_html=True)
with st.sidebar:
    # Other sidebar elements
    # st.sidebar.image("logo_image.png", width=200, use_column_width=True)
    # Option menu in sidebar
    pages = ["About me", "Resume", "Experience",  "Projects","Contact"]
    nav_tab_op = option_menu(
        menu_title="Ayush",
        options=pages,
        icons=['person-fill', 'file-text', 'briefcase', 'folder', 'star', 'envelope'],
        menu_icon="cast",
        default_index=0,
    )
# Main content of the app
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


