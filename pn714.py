import streamlit as st
st.header("BMI METER")
weight = st.number_input('Weight(kg)',min_value=1.0)
height = st.number_input('Height(cm)',min_value=1.0)
if st.button("Calculate BMI"):
    bmi = weight/(height/100)**2
    st.write(f,"BMI Value:{bmi:.2f}")
    if bmi<18.5:
        st.warning('Underweight')
    elif bmi<25:
        st.success("Normal")
    elif bmi<30:
        st.warning("Overweight")
    else:
        st.error("Obese")
    
