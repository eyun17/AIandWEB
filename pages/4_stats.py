import streamlit as st
import pandas as pd

st.title("Game Statistics")

# Ensure that the game-related session state variables exist
if "user_stats" not in st.session_state:
    st.session_state.user_stats = {}

# Input for user name
user_name = st.text_input("Enter your name to view your stats:", key="user_stats_input")

if user_name:
    # Ensure stats exist for the entered user
    if user_name not in st.session_state.user_stats:
        # Initialize user stats for the entered user
        st.session_state.user_stats[user_name] = {
            "games_played": 0,
            "guesses_per_game": [],
            "guess_history": []
        }

    # Extract user-specific data
    user_data = st.session_state.user_stats[user_name]

    # Update `user_stats` based on data from `play.py`
    user_data["games_played"] = st.session_state.games_played
    user_data["guesses_per_game"] = st.session_state.guesses_per_game
    user_data["guess_history"] = [
        entry for entry in st.session_state.guess_history if entry["user_name"] == user_name
    ]

    # Display user-specific statistics
    if user_data["games_played"] > 0:
        st.write(f"User: {user_name}")
        st.write(f"Total Games Played: {user_data['games_played']}")

        # Calculate average guesses per game for this user
        average_guesses = sum(user_data["guesses_per_game"]) / len(user_data["guesses_per_game"])
        st.write(f"Average Guesses per Game: {average_guesses:.2f}")

        # Display a bar chart of guesses per game
        st.bar_chart(user_data["guesses_per_game"], width=0, height=400)

        # Convert guess history to a DataFrame
        guess_history_df = pd.DataFrame(user_data["guess_history"])
        st.write("Guess History:")
        st.dataframe(guess_history_df)
    else:
        st.write(f"No games played yet for {user_name}.")
else:
    st.write("Please enter a name to view statistics.")
