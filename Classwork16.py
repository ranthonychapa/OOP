import streamlit as st
from PIL import Image

col1, col2 = st.columns((4,5))

with col1:
    st.title('My Resume')
    st.header('Justus Selwyn')
with col2:
    image = Image.open('happy.jpg')
    st.image(image, width=200)

st.divider()

st.markdown('**About Me**')
st.text('I am an Academician, Researcher, and a Musician.')
st.text('I am currently working with JBU')
st.divider()

st.markdown('**Contact Me:**')
st.text_input('Your Name:')
st.text_input('Your EmailID:')
st.text_area('Your Message for me:')
st.button('Send Message')