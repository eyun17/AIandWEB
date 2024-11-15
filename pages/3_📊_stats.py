import streamlit as st
import pandas as pd

st.title("Game Statistics")
"""
# Check if stats are available
if "guess_count" in st.session_state:
    st.write(f"Total Guesses: {st.session_state.guess_count}")
    st.write("Guess History:", st.session_state.guess_history)

    # Example: Average guesses (if you’re adding more rounds or resetting)
    if st.session_state.guess_count > 0:
        average_guess = sum(st.session_state.guess_history) / st.session_state.guess_count
        st.write(f"Average Guess: {average_guess:.2f}")
else:
    st.write("No statistics available. Start a game to see stats.")
"""

# Check if there are any recorded games
if "guesses_per_game" in st.session_state and st.session_state.guesses_per_game:
    # Display statistics
    st.write(f"Total Games Played: {st.session_state.games_played}")
    average_guesses = sum(st.session_state.guesses_per_game) / len(st.session_state.guesses_per_game)
    st.write(f"Average Guesses per Game: {average_guesses:.2f}")

    # Display a bar chart of guesses per game
    st.bar_chart(st.session_state.guesses_per_game, width=0, height=400)

    # Convert guess history to a DataFrame
    guess_history_df = pd.DataFrame(st.session_state.guess_history)
    st.write("Guess History:")
    st.dataframe(guess_history_df)
else:
    st.write("No games played yet.")