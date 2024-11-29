import streamlit as st
import random
from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Retrieve the OpenAI API key from the environment variables
openai_api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=openai_api_key)

st.title(f"Hi! {st.session_state.game_user}! Here we are playing the animal guessing game!")
st.write("I am thinking of an animal, and you will ask me questions to guess it. "
         "I can only answer with 'yes' or 'no'.")

# Function to interact with LLM for the animal guessing game
def get_llm_response(prompt):
    response = client.Completion.create(
        engine="gpt-4o-mini",
        prompt=prompt,
        max_tokens=100
    )
    return response.choices[0].text.strip()


# Function to initialize and play the game
def start_game():
    # Initialize the game if it hasn't started
    if "game_started" not in st.session_state:
        st.session_state.game_started = True
        st.session_state.chat_history = []
        st.session_state.animal = random.choice(
            ["cat", "dog", "elephant", "lion", "tiger"])  # Random animal for this game

    # Introduction to the game
    st.title("Animal Guessing Game")
    st.write("I am thinking of an animal, and you will try to guess it!")

    # Displaying chat history
    for msg in st.session_state.chat_history:
        st.chat_message(msg["role"]).markdown(msg["message"])

    # User input for guessing the animal
    user_guess = st.text_input("What is your guess? (Type the animal name)", key="user_name_input")

    if user_guess:
        # AI responds with 'yes' or 'no'
        if user_guess.lower() == st.session_state.animal.lower():
            ai_response = "Yes, that's correct! Well done!"
        else:
            ai_response = "No, that's not correct. Try again!"

        # Append the user guess and AI response to the chat history
        st.session_state.chat_history.append({"role": "user", "message": f"Is it a {user_guess}?"})
        st.session_state.chat_history.append({"role": "assistant", "message": ai_response})

        # Display AI response
        st.chat_message("assistant").markdown(ai_response)

        # Option to start a new game
        if ai_response.startswith("Yes"):
            if st.button("Start a New Game"):
                st.session_state.game_started = False
                st.session_state.chat_history = []
