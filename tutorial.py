import streamlit as st
import pandas as pd
st.title("This is steamlit tutorial")
st.header("Welcome to steamlit")
st.subheader("This is subheader ")
st.text("this is st.text")
st.write("This is st.write")
st.markdown("This is st.markdown")
st.write("biju koi navu")
code = """
def add(a,b):
    return a+b
print(add(5,6))

"""
st.code(code,language='python')
st.sidebar.header("Profile setting")
name = st.sidebar.text_input("Faculty name")
dept = st.sidebar.selectbox("Dept",['CE','CSE','IT'])
col1,col2 = st.columns([1,2])
with col1:
    st.write("basic info")
    st.write(name,dept)
with col2:
    st.subheader("About")
    st.write("A new text")
with st.expander("Subject taught"):
    st.write("Python,CN,DE")
course = st.selectbox("course",['python','FSD','DE'])
days = st.multiselect("Prefered Days",['python','FSD','DE'])
lec = st.radio("Lecture No",[1,2,3])

from datetime import date,time
examdate = st.date_input("Exam Date",date.today())
starttime = st.time_input("Start Time",time(14,0))
file = st.file_uploader("Upload CSV",type=["CSV"])

# Media data 
st.subheader("WebImage")
st.image("https://picsum.photos/600/300",caption="Random Image", use_container_width=True)

st.subheader("Local Image")
st.image("Screenshot 2025-02-21 100030.png")

st.subheader("Audio")
st.audio("audio.mp3")
st.subheader("Video")
st.video("video.mp4")

#Create data 
import pandas as pd
data = {"Student":['A','B','C','D'],"Marks":[85,33,56,77],"Passed":[True,True,True,False]}
df = pd.DataFrame(data)
st.header("st.dataframe")
st.dataframe(df)
st.header("st.table")
st.table(df)
#json
st.subheader("JSON-JAVASCRIPT OBJECT NOTATION")
st.json(data)

import time 
st.info("Useful Information")
if st.button("Start Long Run"):
    progress = st.progress(0)
    with st.spinner("Processing"):
        for i in range(100):
            time.sleep(0.03)
            progress.progress(i+1)
    st.success("Task Completed")
    st.balloons()
#CHARTS
st.header("MAtplotlib based Charts")
import matplotlib.pyplot as plt
import numpy as np
x = np.arange(1,11)
y = np.random.randint(50,100,size=10)
plt.figure(figsize=(6,4))
plt.plot(x,y,'*')
plt.xlabel('Xaxis')
plt.ylabel('yaxis')
plt.title('Matplotlib based line chart')
st.pyplot(plt)

# 
st.header("Streamlit based chart")
df1 = pd.DataFrame(
    {
        'Student':x,
        'Marks' :y
    }
)
st.line_chart(df1)
