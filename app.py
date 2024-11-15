import streamlit as st
import random
import datetime
import time


# Set up a title for the main page
st.title("Welcome to the Guessing Game App")

# Sidebar custom navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to:", ["Home", "Play Game", "Statistics"])

# Navigate to the selected page
if page == "Home":
    st.write("Welcome to the Guessing Game! Choose a page to get started.")
elif page == "Play Game":
    st.session_state.current_page = "pages/2_🕹_play.py"
    st.rerun()
elif page == "Statistics":
    st.session_state.current_page = "pages/3_📊_stats.py"
    st.rerun()
