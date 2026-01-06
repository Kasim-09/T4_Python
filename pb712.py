import streamlit as st
st.header("PB 712 Program")
with st.sidebar:
    country = st.selectbox("Select country",['USA','India','Uk','Canada'])
    # st.write('kasim')
totalpopulation = st.number_input("Enter population",min_value=1)
vaccinated = st.number_input("Vaccinated people",min_value=0)
if st.button("Calculate Vaccination"):
    percentage = (vaccinated/totalpopulation)*100
    st.write(f"Vaccinated for {country} is {percentage:.2f}%")
    st.progress(min(int(percentage),100))
    if percentage >= 70:
        st.success("GOOD VACINATION")
    else:
        st.warning("VACCINATION IS POOR")
