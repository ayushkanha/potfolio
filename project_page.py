import streamlit as st
import json
from streamlit_lottie import st_lottie

def projects():
    col1, col2 = st.columns(2)

    # col1.markdown("## Experience")
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
                    <h2>Projects </h2>
                </div>
            """, unsafe_allow_html=True)
    path = "Animation - 1732430682998.json"
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
        col1,col2 = st.columns(2)
        with col1:
            with st.container(border=True):


                # Displaying the title of the project
                st.title("Movies Recommendation System")

                # Displaying the description
                st.markdown("""
                **Description:**
                Built a recommendation engine that suggests movies based on the user's watched history.Integrated TMDB Dataset and API to fetch detailed movie information and high-quality images.Deployed the application on Streamlit Cloud for easy access and interaction. Key features include:
                - **Personalized Recommendations:** Suggests movies based on user preferences, genres, and popularity.
                - **Enhanced User Experience:** Displays movie posters and details (like release date, rating, and overview) using TMDB API.
                - **Collaborative Filtering:** Employs advanced techniques like cosine similarity to provide accurate suggestions.
                - **Interactive Interface:** Allows users to input their favorite movies and receive tailored recommendations.
                """)

                # Displaying the tools used
                st.markdown("""
                **Tools Used:**
                
                 **Python** ,
                 **Pandas**,
                **Streamlit** ,
                **TMDB Dataset and API**, 
                """)
                st.markdown(""" """)


                c1,c2 = st.columns(2)
                c1.markdown("""**[Link to app](https://movie-recommendation-ayush.streamlit.app/)**  """)
                c2.markdown("""**[GitHub](https://github.com/ayushkanha/Movie_recommendation)**""")
                

        with col2:
            with st.container(border=True):
                st.markdown(""" """)
                
                # Displaying the title of the project
                st.title("Whatsapp Chat Analysis")
                st.markdown(""" """)
                st.markdown(""" """)


                # Displaying the description
                st.markdown("""
                **Description:**
                The Insightful Data Explorer is a Streamlit-based application designed for Extracts meaningful insights such as user activity, sentiment analysis, and word frequency. Key features include:
                
                - **Chat Statistics:** Provides insights like total messages, media shared, and participant activity.
                - **Interactive Visualizations:** Utilized Matplotlib and Seaborn to create visually appealing charts and graphs.
                - **Keyword Analysis:** Highlights the most used words and emojis in the conversation.
                - **Sentiment Analysis:** Determines the overall tone of the chats using natural language processing techniques.
                - **Customizable Uploads:** Allows users to upload their chat export files for personalized analysis.
                
                """)
                


                # Displaying the tools used
                st.markdown("""
                **Tools Used:**

                **Python**, 
                **Streamlit**,  **Plotly**, **Pandas**
                
                """)
               
                st.markdown(""" """)


                c1, c2 = st.columns(2)
                c1.markdown("""**[Link to app](https://whatsapp-analysis-ayush-projects.streamlit.app/)**  """)
                c2.markdown("""**[GitHub](https://github.com/ayushkanha/Whatsapp-Analysis)**""")
                
               
                
                
                


        with col1:
            with st.container(border=True):
                # Displaying the title of the project
                st.title("Student Result Management System")

                # Displaying the description
                st.markdown("""
                **Description:**
                Developed a web-based application for managing and displaying student results.Designed an intuitive interface to streamline result generation and access.

                ***Key Features:***

                - **Admin Panel:** Allows administrators to add, edit, and manage student records and grades.
                - **Student Access:** Enables students to view their results by entering credentials.
                - **Secure Authentication:** Ensures data security using role-based access controls.
                - **Dynamic Updates:** Results can be updated or modified in real-time through the admin interface.
                """)
                st.markdown(""" """)



                # Displaying the tools used
                st.markdown("""
                ***Tools & Technologies:***
                - **Frontend:** HTML, CSS, JavaScript for responsive and interactive design.
                - **Backend:** PHP for server-side processing and MySQL for database management.
                - **Database:** Structured student and result records stored in MySQL.
                """)
                st.markdown(""" """)
                
                

                # Adding the GitHub link
                st.markdown("""**[GitHub](https://github.com/ayushkanha/SRMS)**""")

        with col2:
            with st.container(border=True):
                # Displaying the title of the project
                st.title("E-Pharmacy Website")

                # Displaying the description
                st.markdown("""
                **Description:**
                Designed and developed a comprehensive e-pharmacy platform combining standard online pharmacy features with advanced capabilities like price comparison and location services.Integrated MapmyIndia API to help users locate nearby pharmacies and hospitals with detailed information.
                ***Key Features:***

                - **Pharmacy Services**: Supports product browsing, searching, and purchasing of medicines and health products.
                - **Price Comparison**: Compares product prices across multiple platforms to help users find the best deals.
                - **Location Services**: Displays nearby pharmacies and hospitals on a map with their addresses and contact details.
                - **Responsive Design**: Built with React for a seamless and intuitive user experience on both desktop and mobile devices.
                """)
                st.markdown(""" """)


                # Displaying the tools used
                st.markdown("""
                ***Tools & Technologies:***

                **Frontend:** React for dynamic and responsive UI development.
                **Backend:** Python for server-side logic and APIs.
                **Map Integration:** MapmyIndia API for location-based services.
                
                """)
                st.markdown(""" """)


                # Adding the GitHub link
                st.markdown("""**[GitHub](https://github.com/ayushkanha/E-pharmacy)**""")

        with col1:
            with st.container(border=True):
                st.markdown(""" """)

                # Displaying the title of the project
                st.title("Password Manager App")
                st.markdown(""" """)
                



                # Displaying the description
                st.markdown("""
                **Description:**
                Developed a secure and user-friendly password manager application using Python.Implemented Fernet encryption, a symmetric key encryption algorithm, to ensure data security.Integrated MongoDB Atlas for scalable and reliable data storage.
               **Key Features:**

               - **Password Storage:** Safely stores passwords for multiple accounts with encryption.
               - **Encryption/Decryption:** Encrypts passwords using the Fernet algorithm and decrypts them on demand.
               - **User-Friendly Interface:** Built an interactive GUI with Tkinter for easy navigation and usability.
               - **Cross-Platform Support:** Ensures compatibility across various operating systems.
                """)
                st.markdown(""" """)

                # Displaying the tools used
                st.markdown("""
                **Tools & Technologies:**

                - **Frontend:** Custom Tkinter library for building the graphical user interface.
                - **Encryption:** Fernet (from Python’s Cryptography library) for secure data handling.
                - **Database:** MongoDB Atlas for storing encrypted data with high availability and scalability.
                """)
                
                st.markdown(""" """)
                # Adding the GitHub link
                st.markdown("""**[GitHub](https://github.com/ayushkanha/Passsword-manager)**""")
                st.markdown(""" """)
        
        with col2:
            with st.container(border=True):
                # Displaying the title of the project
                st.title("Portfolio Explorer ")

                # Displaying the description
                st.markdown("""
                **Description:**
                The Portfolio Explorer is a Streamlit-based application designed to present a comprehensive and interactive personal portfolio. Key features include:

                - **Intro Page:** A dynamic introduction offering a professional overview.
                - **Resume Page:** A viewable and downloadable resume for quick access to detailed professional information.
                - **Experience Page:** An organized display of work experience, skills, and accomplishments.
                - **Projects Page:** A showcase of notable projects, including descriptions, technologies used, and links to repositories.
                - **Contact Page:** An integrated contact form for easy communication and inquiries.
                """)

                # Displaying the tools used
                st.markdown("""
                **Tools Used:**

                **Python** , **Streamlit**
                """)
                st.markdown(""" """)

                c1, c2 = st.columns(2)


                # Adding the GitHub link
                c1.markdown("""**[Link to app](https://github.com/ayushkanha/potfolio)**  """)
                c2.markdown("""**[GitHub](https://potfolio-ayush.streamlit.app/)**""")

       

