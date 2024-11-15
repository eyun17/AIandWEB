import streamlit as st
import random

def play_page():
    st.title("Guessing Game")
    st.write("Try to guess the animal I'm thinking of!")

    # Initialize session state for guesses
    if 'guesses' not in st.session_state:
        st.session_state.guesses = []
    if 'goal' not in st.session_state:
        st.session_state.goal = "elephant"  # For simplicity, the animal to guess is "elephant"

    # Get user's guess from the chat input
    guess = st.chat_input("What's your guess?")

    # Process guess
    if guess:
        st.session_state.guesses.append(guess)
        if guess.lower() == st.session_state.goal:
            st.write("🎉 Correct! You've guessed it!")
            st.session_state.games_played += 1
            st.session_state.total_guesses += len(st.session_state.guesses)
            st.session_state.guesses = []  # Reset guesses for new game
        else:
            st.write("❌ Incorrect, try again!")


# Navigate to Play Page
if st.sidebar.button("Play"):
    play_page()


def stats_page():
    st.title("Game Stats")
    games_played = st.session_state.get('games_played', 0)
    total_guesses = st.session_state.get('total_guesses', 0)
    avg_guesses = total_guesses / games_played if games_played > 0 else 0

    # Display stats
    st.write(f"Games Played: {games_played}")
    st.write(f"Average Guesses per Game: {avg_guesses:.2f}")

    # Bar Chart for guesses per game
    if 'guess_history' in st.session_state:
        fig, ax = plt.subplots()
        ax.bar(range(1, games_played + 1), st.session_state.guess_history)
        ax.set_xlabel("Game")
        ax.set_ylabel("Number of Guesses")
        st.pyplot(fig)
    else:
        st.write("No games played yet.")


# Navigate to Stats Page
if st.sidebar.button("Stats"):
    stats_page()
