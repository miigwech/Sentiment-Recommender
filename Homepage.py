import streamlit as st 


st.set_page_config(
    page_title="MoodSync Sentiment Recommender",
    page_icon="🤖"
)

st.title("MoodSync")
sidebar = st.sidebar.success("Select the recommender above")

st.markdown('This project aims to develop an emotion-based recommendation system that can recommend songs to users based on their current mood.')

# Display information about the project, such as the team members, the technologies used, and the project goals.
st.markdown('**Team members:**')
st.markdown('- ADITYA SAWANT')
st.markdown('- SARVESH MORE')
st.markdown('- HARSH PANDEY')
st.markdown('- SAMRUDHI BHADARGE')


st.markdown('**Technologies used:**')
st.markdown('- Python')
st.markdown('- Streamlit')
st.markdown('- OpenCV')
st.markdown('- FER')

st.markdown('**Project goals:**')
st.markdown('- Develop a working emotion-based recommendation system.')
st.markdown('- Make the system easy to use and accessible to everyone.')
st.markdown('- Integrate the system with music, movies , book recommendations and inbulit chatbot services.')



