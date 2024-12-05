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
            "games_won": 0,
            "games_lost": 0,
            "guesses_per_game": [],
            "questions_per_game": [],
            "guess_history": [],
            "total_questions_answered": 0,
            "total_guesses_made": 0
        }

    # Extract user-specific data
    user_data = st.session_state.user_stats[user_name]

    # Update `user_stats` based on data from `play.py`
    if "games_played" in st.session_state:
        user_data["games_played"] = st.session_state.games_played
    if "games_won" in st.session_state:
        user_data["games_won"] = st.session_state.won_game
    if "games_lost" in st.session_state:
        user_data["games_lost"] = st.session_state.lost_game
    if "guesses_per_game" in st.session_state:
        user_data["guesses_per_game"] = st.session_state.guesses_per_game
    if "questions_per_game" in st.session_state:
        user_data["questions_per_game"] = st.session_state.total_questions_per_game
    if "guess_history" in st.session_state:
        user_data["guess_history"] = st.session_state.guess_history
    if "total_questions_answered" in st.session_state:
        user_data["total_questions_answered"] = st.session_state.total_questions_answered
    if "total_guesses_made" in st.session_state:
        user_data["total_guesses_made"] = st.session_state.total_guesses_made

    # Display user-specific statistics
    if user_data["games_played"] > 0:
        st.write(f"User: {user_name}")
        st.write(f"Total Games Played: {user_data['games_played']}")
        st.write(f"Games Won: {user_data['games_won']}")
        st.write(f"Games Lost: {user_data['games_lost']}")

        # Calculate average guesses per game for this user
        if user_data["games_played"] > 0:
            average_guesses = sum(user_data["guesses_per_game"]) / len(user_data["guesses_per_game"])
            st.write(f"Average Guesses per Game: {average_guesses:.2f}")

        # Calculate average questions per game
        if user_data["games_played"] > 0:
            average_questions = sum(user_data["questions_per_game"]) / len(user_data["questions_per_game"])
            st.write(f"Average Questions per Game: {average_questions:.2f}")

        # Display a bar chart of guesses per game
        st.bar_chart(user_data["guesses_per_game"], width=0, height=400)

        # Display a bar chart of questions per game
        st.bar_chart(user_data["questions_per_game"], width=0, height=400)

        # Convert guess history to a DataFrame
        guess_history_df = pd.DataFrame(user_data["guess_history"])
        st.write("Guess History:")
        st.dataframe(guess_history_df)

        # Show total questions answered and guesses made
        st.write(f"Total Questions Answered: {user_data['total_questions_answered']}")
        st.write(f"Total Guesses Made: {user_data['total_guesses_made']}")

    else:
        st.write(f"No games played yet for {user_name}.")
else:
    st.write("Please enter a name to view statistics."