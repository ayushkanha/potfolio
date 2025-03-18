import streamlit as st
import json
from streamlit_lottie import st_lottie

def projects():
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
                <style>
                .centered {
                    display: flex;
                    align-items: center;
                    height: 100%;
                    margin-top: 200px;
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
        st_lottie(url, reverse=True, height=400, width=400, speed=1, loop=True, quality='high')

    with st.container():
        col1, col2 = st.columns(2)

        # Existing Projects (No Changes)
        with col1:
            with st.container(border=True):
                st.title("Movies Recommendation System")
                st.markdown("""
                **Description:**
                Built a recommendation engine that suggests movies based on the user's watched history. Integrated TMDB Dataset and API to fetch detailed movie information and high-quality images. Deployed the application on Streamlit Cloud for easy access and interaction.

                - **Personalized Recommendations**: Suggests movies based on user preferences, genres, and popularity.
                - **Enhanced User Experience**: Displays movie posters and details (like release date, rating, and overview) using TMDB API.
                - **Collaborative Filtering**: Uses cosine similarity to provide accurate suggestions.
                - **Interactive Interface**: Allows users to input their favorite movies and receive tailored recommendations.
                """)

                st.markdown("**Tools Used:** Python, Pandas, Streamlit, TMDB Dataset and API")
                c1, c2 = st.columns(2)
                c1.markdown("**[Link to app](https://movie-recommendation-ayush.streamlit.app/)**")
                c2.markdown("**[GitHub](https://github.com/ayushkanha/Movie_recommendation)**")

        with col2:
            with st.container(border=True):
                st.title("WhatsApp Chat Analysis")
                st.markdown("""
                **Description:**
                A Streamlit-based application that extracts meaningful insights such as user activity, sentiment analysis, and word frequency from WhatsApp chat data.

                - **Chat Statistics**: Provides insights like total messages, media shared, and participant activity.
                - **Interactive Visualizations**: Uses Matplotlib and Seaborn to create visually appealing charts and graphs.
                - **Keyword Analysis**: Highlights the most used words and emojis.
                - **Sentiment Analysis**: Determines the overall tone of chats using NLP techniques.
                - **Customizable Uploads**: Allows users to upload chat export files for personalized analysis.
                """)

                st.markdown("**Tools Used:** Python, Streamlit, Plotly, Pandas")
                c1, c2 = st.columns(2)
                c1.markdown("**[Link to app](https://whatsapp-analysis-ayush-projects.streamlit.app/)**")
                c2.markdown("**[GitHub](https://github.com/ayushkanha/Whatsapp-Analysis)**")

        # New Projects
        with col1:
            with st.container(border=True):
                st.title("Vendor Analysis Dashboard")
                st.markdown("""
                **Description:**
                Developed a vendor analysis tool to track and evaluate vendor performance based on sales, pricing trends, and reliability.

                - **Performance Metrics**: Tracks vendor reliability, sales volume, and delivery time efficiency.
                - **Price Comparisons**: Compares product prices across different vendors to identify the best deals.
                - **Interactive Data Visualization**: Provides dynamic dashboards using Power BI and Python.
                - **Trend Analysis**: Identifies patterns in vendor performance over time.
                """)

                st.markdown("**Tools Used:** Python, Pandas, Streamlit, SQL")
                c1.markdown("""**[Link to app](https://vendoranalytics.streamlit.app/)**  """)
                st.markdown("**[GitHub](https://github.com/ayushkanha/Vendor_analytics)**")

        with col2:
            with st.container(border=True):
                st.title("Speech-to-Speech Translator")
                st.markdown("""
                **Description:**
                A real-time speech translation application that converts spoken words from one language to another.

                - **Speech Recognition** : Converts speech into text using Google Speech Recognition API from mic, uploaded audio, or text input.
                - **Language Translation** : Translates text into multiple languages using GoogleTranslator for seamless communication.
                - **Text-to-Speech** : Converts translated text into speech using gTTS, providing an audio output.
                - **Real-Time Processing** : Ensures low-latency transcription, translation, and speech synthesis for smooth interaction.
                - **Sentiment Analysis** : Analyzes sentiment using Hugging Face Transformers and classifies text into five categories.
                - **User-Friendly UI** : Built with Streamlit, featuring an interactive interface with custom-styled elements.
                """)

                st.markdown("**Tools Used:** Python, Hugging Face, Google Speech API, Streamlit")
                c1, c2 = st.columns(2)
                c1.markdown("""**[Link to app](https://speech-speech-ayush.streamlit.app/)**  """)
                c1.markdown("**[GitHub](https://github.com/ayushkanha/Translate-speach)**")

        with col1:
            with st.container(border=True):
                st.title("E-Pharmacy Price Comparison System")
                st.markdown("""
                **Description:**
                Developed a price comparison platform that fetches and compares product prices across multiple e-commerce websites.

                - **Medicine Price Comparison** : Fetches and compares medicine prices from various online vendors using SerpAPI.
                - **Best Price Selection** : Identifies and highlights the lowest-priced option among available vendors.
                - **Vendor Analysis** : Displays price variations across different sellers with detailed breakdowns.
                - **Interactive UI** : Streamlit-based interface for an intuitive and user-friendly experience.
                - **Data Visualization** : Provides bar and pie charts for easy comparison of price differences.
                - **Direct Purchase Links** : Offers clickable links to buy medicines directly from vendors.
                """)

                st.markdown("**Tools Used:** Python, Streamlit, SerpAPI, Pandas, Matplotlib ")
                c1.markdown("""**[Link to app](https://pricecompair.streamlit.app/)**  """)
                st.markdown("**[GitHub](https://github.com/ayushkanha/price_compair)**")
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
                c1.markdown("""**[Link to app](https://potfolio-ayush.streamlit.app/)**  """)
                c2.markdown("""**[GitHub](https://github.com/ayushkanha/potfolio)**""")
       

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
