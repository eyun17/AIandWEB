import streamlit as st
import random

st.title("Here we are playing the guessing game")

# Initialize session variables if not already done
if "user_guess" not in st.session_state:
    st.session_state.user_guess = 0
if "guess_history" not in st.session_state:
    st.session_state.guess_history = []
if "guess_count" not in st.session_state:
    st.session_state.guess_count = 0
if "games_played" not in st.session_state:
    st.session_state.games_played = 0
if "guesses_per_game" not in st.session_state:
    st.session_state.guesses_per_game = []
if "secret_number" not in st.session_state:
    st.session_state.secret_number = random.randint(0, 100)

# Get user input
user_guess = st.number_input("Pick a number between 0 and 100", 0, 100, st.session_state.user_guess)
submit = st.button("Submit")

if submit:
    st.write("You entered:", user_guess)
    # Update session variables
    st.session_state.guess_count += 1
    # Track each guess in guess history with game number and guess count
    st.session_state.guess_history.append({
        "game_number": st.session_state.games_played + 1,
        "guess_number": st.session_state.guess_count,
        "guess": user_guess
    })

    # Check if guess is correct
    if user_guess == st.session_state.secret_number:
        st.session_state.guesses_per_game.append(st.session_state.guess_count)
        st.session_state.games_played += 1
        st.session_state.guess_count = 0  # Reset for the next game
        st.session_state.secret_number = random.randint(0, 100)  # New secret number
        st.write("🎉 You guessed it!")
    elif user_guess < st.session_state.secret_number:
        st.write("Try a higher number")
    else:
        st.write("Try a lower number")