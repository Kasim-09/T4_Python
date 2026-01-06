import streamlit as st
import numpy as np
st.header("PB 711 APP")
name = st.text_input("Enter Name - ")
age = st.slider("Select Age",10,100)
gender = st.radio("Choose gender",['male','female','other'])
hobbies = st.multiselect("Select hobbies",['Reading','Gaming','Playing','Eating','Sleeping'])
photo = st.file_uploader("Upload Pic",['png','jpg','jpeg'])
if st.button("Submit Profile"):
    st.subheader("Profile Details - ")
    st.write("Name",name)
    st.write("age",age)
    st.write("Gender",gender)
    st.write("Hobbies",','.join(hobbies))
    if photo:
        st.image(photo,caption="Profile pic",width=200)
