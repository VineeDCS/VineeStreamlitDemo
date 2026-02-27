import streamlit as st
 
st.title("📊 Dashboard Page")
 
st.write("This is the Dashboard page.")
 
# Example content
number = st.slider("Select a number:", 0, 100, 50)
st.write("Selected value:", number)
 
if st.button("Show Message"):
    st.success("Dashboard Button Clicked!")