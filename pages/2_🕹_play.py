import streamlit as st
import random

st.title(f"Hi! {st.session_state.game_user}! Here we are playing the guessing game")

if st.button("Reset Username"):
    # Remove current user's data from user_stats
    if st.session_state.game_user in st.session_state.user_stats:
        del st.session_state.user_stats[st.session_state.game_user]

    # Clear the active username
    st.session_state.game_user = None
    st.rerun()  # Refresh the app to go back to the username input screen

# Initialize session variables if not already done
if "secret_number" not in st.session_state:
    st.session_state.secret_number = random.randint(0, 100)
if "games_played" not in st.session_state:
    st.session_state.games_played = 0
if "guess_count" not in st.session_state:
    st.session_state.guess_count = 0
if "guesses_per_game" not in st.session_state:
    st.session_state.guesses_per_game = []
if "user_guess" not in st.session_state:
    st.session_state.user_guess = 0
if "guess_history" not in st.session_state:
    st.session_state.guess_history = []


# Get user input
user_guess = st.number_input("Pick a number between 0 and 100", 0, 100, st.session_state.user_guess)
submit = st.button("Submit")

if submit:
    st.write("You entered:", user_guess)
    # Update session variables
    st.session_state.guess_count += 1
    # Track each guess in guess history with game number and guess count
    st.session_state.guess_history.append({
        "user_name": st.session_state.game_user,
        "game_number": st.session_state.games_played + 1,
        "secret_number": st.session_state.secret_number,
        "guess_number": st.session_state.guess_count,
        "guess": user_guess
    })

    # Check if guess is correct
    if user_guess == st.session_state.secret_number:
        # Save the number of guesses for this game
        st.session_state.guesses_per_game.append(st.session_state.guess_count)
        # Increment games played
        st.session_state.games_played += 1

        # Reset for the next game
        st.session_state.guess_count = 0
        # New Secret Number
        st.session_state.secret_number = random.randint(0, 100)
        st.write("🎉 You guessed it!")
    elif user_guess < st.session_state.secret_number:
        st.write("Try a higher number")
    else:
        st.write("Try a lower number")