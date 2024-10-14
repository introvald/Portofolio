import streamlit as st

# Function for the main profile page
def main_profile():
    st.title("Muhammad Rafi Danendra Putra")
    st.header("Profile")
    st.write("""
Halo, saya Danen. Saya memiliki ketertarikan yang mendalam dalam ilmu machine learning, yang merupakan bagian dari Artificial Intelligence. Saya berharap suatu hari dapat berkarier sebagai AI Engineer. Untuk meningkatkan pengetahuan dan keterampilan saya, saya sering mengikuti kursus-kursus seperti Dicoding, IDCamp, dan Google Skill Boost.
    """)
    st.image("Foto Muhammad Rafi danendra.jpg", caption='me', width=200)
  
    st.subheader("Skills")
    st.write("- Python")
    st.write("- Streamlit")
    st.write("- Data Analysis")
    st.write("- Machine Learning")

# Function for the projects page
def projects():
    st.title("My Projects")
    st.header("Project 1: Speech-to-Text Web App")
    st.write("""
        A web application that converts speech to text using Streamlit and speech recognition APIs.
        - Technologies Used: Streamlit, SpeechRecognition, Python
        - GitHub Link: [Speech to Text](https://github.com/introvald/speech-to-text)  
    """)
    
    st.header("Project 2: Prediksi-Diabetes Web App")
    st.write("""
        A web application for predicting diabetes risk based on user input.
        - Technologies Used: Streamlit, Sklearn preprocessing, Python
        - GitHub Link: [Predict Diabetes App](https://github.com/introvald/App-Predict-Diabetes)  
    """)

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Select a page", ("Profile", "Projects"))

# Render the selected page
if page == "Profile":
    main_profile()
elif page == "Projects":
    projects()
