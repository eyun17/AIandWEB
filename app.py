import streamlit as st
import random
import datetime
import time

# Set up the page configuration
#st.set_page_config(
#    page_title="Main Page",
#    page_icon="👋",
#)

# Set up a title for the main page
st.title("Welcome to the Guessing Game App")

# Check if the 'game_user' is set in session state
if 'game_user' not in st.session_state:
    st.session_state.game_user = None

if st.session_state.game_user is None:
    # If the user is not set, ask for their name
    st.title("Welcome to the Guessing Game!")
    st.write("Please enter your name to start playing.")

    # Create a unique key for the name input field by appending a string like 'name_input_1'
    user_name = st.text_input("Enter your name", key="name_input")

    # Button to confirm the name
    if st.button("Start Game"):
        if user_name:
            # Save the name to session state
            st.session_state.game_user = user_name
            st.success(f"Welcome, {st.session_state.game_user}! Let's start playing!")
        else:
            st.error("Please enter a right name to proceed.")
else:
    # Now that the user has entered their name, show the available pages
    st.title(f"Hello, {st.session_state.game_user}!")
    st.write("You can now access the game pages using the navigation sidebar.")

