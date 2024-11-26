import streamlit as st
from streamlit_lottie import st_lottie
import json

def experience():
    col1,col2 =st.columns(2)

    with col1:
        st.markdown("""
            <style>
            .centered {
                display: flex;
                align-items: center;
                height: 100%;
                margin-top: 200px; /* Adjust this value as needed */
            }
            </style>
            <div class="centered">
                <h2>Experience</h2>
            </div>
        """, unsafe_allow_html=True)
    path = "exp.json"
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
    with st.container():
        col1,col2 = st.columns([3,2])
        col1.markdown(""" 
            ### Assistant Intern –– [The iScale](https://www.linkedin.com/company/theiscale/)
            ### (Sep. 2024 – Present)
            - Developing and delivering end-to-end Data Science projects as course content to facilitate hands-on learning for
            students.
            - Assisting students in resolving technical questions, reinforcing their understanding of key concepts in data science,
            analytics, and programming.
            - Continuously enhancing my skill set by learning and implementing new tools, techniques, and methodologies in
            data science.
                    """)
        col2.markdown("""
            **Tools:**

            - Programming Languages: Python, SQL
            - Machine Learning: Scikit-Learn, TensorFlow
            - Data Visualization: Matplotlib, Seaborn, Plotly, Powerbi, Tableau
            - ETL Processes: Custom SQL, Python scripts
            - A/B Testing: Custom Python scripts
            - Other Tools: Git, Colab Notebooks, DAX,Power Query, streamlit
            """)
    st.markdown("  ")
    with st.container():
        col1, col2 = st.columns([3, 2])
        col1.markdown("""
           ### Intern –– [SAIL —BHILAI STEEL PLANT] (August 2024 –September 2024)
    
           - Designed and deployed a scalable framework for E-Medical website, enhancing accessibility and user experience.
           - Collaborated with the team to implement core functionalities, ensuring the platform met client specifications and
            industry standards.
           - Gained hands-on experience with web development and deployment practices in a professional setting.
           """)
        col2.markdown(""" 
        **Tools:**
        
        - Programming Languages: HTML ,CSS ,JS , PYTHON,REACT
        - ETL Processes: Custom SQL, Python scripts
        - Generative AI: LLM, Langchain
        - Other Tools: Git, Jupyter Notebooks, Selenium""")

    # st.markdown()