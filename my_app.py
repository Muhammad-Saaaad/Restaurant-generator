import streamlit as st
import langchain_helper

st.header("Restaurant Name Generator")

cuisine = st.sidebar.selectbox("Pick a Cuisine", ("Pakistani" ,"Indian", "Italian", "japanese" ,"Mexican", "Arabic", "American", "chinese"))

if cuisine:
    try:
        response = langchain_helper.generate_restrunt_menu(cuisine)
        
        # Directly display the response as is
        st.markdown(response)
        
    except Exception as e:
        st.error(f"An error occurred: {e}")
