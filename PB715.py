import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
st.header("APP")
n = st.number_input("Enter number of points",min_value=10,step=10)
if st.button("Generate Scatter plot"):
    x = np.random.rand(n)
    y = np.random.rand(n)
    plt.figure(figsize = (6,4))
    plt.scatter(x,y)
    plt.xlabel("X values")
    plt.ylabel("y values")
    plt.title("Random scatter plot")
    st.pyplot(plt)
