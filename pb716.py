import streamlit as st
st.header('To Do List')
task1 = st.text_input('Task-1')
task2 = st.text_input('Task-2')
task3 = st.text_input('Task-3')
if task1:
    if st.checkbox(task1):
        st.success('Completed Task1')
if task2:
    if st.checkbox(task2):
        st.success('Completed Task2')
if task3:
    if st.checkbox(task3):
        st.success('Completed Task3')
