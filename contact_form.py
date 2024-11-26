import streamlit as st
import streamlit.components.v1 as components
from streamlit_lottie import st_lottie
import json

def contact():
    col1, col2 = st.columns(2)

    # col1.markdown("## Experience")
    with col1:
        st.markdown("""
                    <style>
                    .centered {
                        display: flex;
                        align-items: center;
                        height: 100%;
                        margin-top: 50px;
                    }
                    </style>
                    <div class="centered">
                        <h2>📨 Contact Info. </h2>
                    </div>
                """, unsafe_allow_html=True)
    path = "contact.json"
    with open(path, "r") as file:
        url = json.load(file)
    with col2:
        st_lottie(url,
                  reverse=True,
                  height=200,
                  width=200,
                  speed=1,
                  loop=True,
                  quality='high',
                  )
        
    st.markdown("<h2 style='text-align: left; '>Phone : +91-9479280486</h2>", unsafe_allow_html=True)
    
    url = "ayushkanh19@gmail.com"
    st.header("******Mail : [ayushkanha19@gmail.com](%s)******" % url)
    
    url = "https://linkedin.com/in/ayush-kumar-sahu-299b8b23b"
    st.header("******Linkdin : [Link](%s)******" % url)
    url = "https://github.com/ayushkanha"
    st.header("******Github : [Link](%s)******" % url)


