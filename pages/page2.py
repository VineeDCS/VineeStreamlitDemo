import streamlit as st
 
st.title("📝 Student Registration Form")
 
name = st.text_input("Enter Name:")
age = st.slider("Select Age:", 5, 60, 18)
course = st.selectbox("Select Course:", ["Python", "Data Science", "Cloud"])
subjects = st.multiselect("Select Subjects:", ["Math", "Science", "English"])
 
if st.button("Submit"):
    st.success("Form Submitted Successfully!")
    st.write("Name:", name)
    st.write("Age:", age)
    st.write("Course:", course)
    st.write("Subjects:", subjects)