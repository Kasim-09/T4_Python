import streamlit as st
c1,c2,c3,c4,c5 = st.columns(5)
sub1 = c1.number_input("Marks of subject-1",0,100,0)
sub2 = c2.number_input("Marks of subject-2",0,100,0)
sub3 = c3.number_input("Marks of subject-3",0,100,0)
sub4 = c4.number_input("Marks of subject-4",0,100,0)
sub5 = c5.number_input("Marks of subject-5",0,100,0)
if st.button("Calculate"):
    total_marks = sub1+sub2+sub3+sub4+sub5
    average_marks = total_marks/5
    if average_marks>=60:
        division = 'First Division'
    elif average_marks>=40:
        division = 'second division'
    else:
        division = 'fail'
    with st.expander("results"):
        st.write("Total marks",total_marks)
        st.write("Average - ",average_marks)
        st.write("Division - ",division)
