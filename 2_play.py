import streamlit as st
import random
from openai import OpenAI

# Get the OpenAI API key from Streamlit Secrets and initialize the client
api_key = st.secrets["OPENAI_API_KEY"]
client = OpenAI(api_key=api_key)


# Function to interact with LLM for the animal guessing game
def get_llm_response(question_input):
    question = "Answer the following question in Yes or No only. If not a valid question, answer NA. Do not reveal the animal name. The question is about the animal " + st.session_state.animal + ": " + question_input
    response = client.chat.completions.create(
        model="gpt-4o-mini",  # You can use gpt-4 or other models depending on your access
        messages=[{"role": "user", "content": question}],
        max_tokens=100
    )
    return response.choices[0].message.content

# Function to choose a random animal using OpenAI
def choose_random_animal():
    # Just use Python's random choice from a large list of animals
    animals = [
        "cat", "dog", "elephant", "lion", "tiger", "giraffe", "zebra", "kangaroo", "panda",
        "wolf", "bunny", "rabbit", "koala", "flamingo", "dolphin", "whale", "octopus", "bear",
        "eagle", "shark", "owl"
    ]
    return random.choice(animals)

# Function to generate a hint using the second letter of the animal
def get_hint():
    animal = st.session_state.animal
    if len(animal) > 1:
        second_letter = animal[1].lower()  # Get the second letter
        return f"Hint: The second letter of the animal is '{second_letter}'."
    else:
        return "The animal name is too short to provide a second letter hint."

# Function to initialize and play the game
def start_game():
    # Set up the page configuration
    st.title(f"Hi! {st.session_state.game_user}! Here we are playing the animal guessing game!")
    st.write("I am thinking of an animal, and you will ask me questions to guess it. "
             "I can only answer with 'yes' or 'no'.")

    # Initialize the game if it hasn't started
    if "game_started" not in st.session_state:
        st.session_state.game_started = True
    if "won_game" not in st.session_state:
        st.session_state.won_game = 0
    if "lost_game" not in st.session_state:
        st.session_state.lost_game = 0
    if "questions_remaining" not in st.session_state:
        st.session_state.questions_remaining = 12
    if "guesses_remaining" not in st.session_state:
        st.session_state.guesses_remaining = 3
    if "total_questions" not in st.session_state:
        st.session_state.total_questions = 0

    # Initialize history lists if they don't exist
    if "question_history" not in st.session_state:
        st.session_state.question_history = []  # Stores questions asked
        st.session_state.answer_history = []  # Stores corresponding answers (Yes/No)
        st.session_state.guess_history = []  # Stores guesses
        st.session_state.guess_result_history = []  # Stores guess results (Yes/No)

    # function to reset stats and country and aggregate total stats
    def reset_game_state():
        if st.session_state.total_games > 0:
            st.session_state.guesses_per_game.append(st.session_state.current_game_guesses)
        st.session_state.animal = choose_random_animal()
        st.session_state.guesses_remaining = 3
        st.session_state.questions_remaining = 12
        st.session_state.total_games += 1
        st.session_state.current_game_guesses = 0

    # Introduction to the game
    st.session_state.animal = choose_random_animal()

    st.title("Animal Guessing Game")
    st.write("I am thinking of an animal, and you will try to guess it!"
             "You can ask me max 10 questions to help you guess the animal."
             "You have 3 guesses to guess the animal. Good luck!")

    # button to reset game
    if st.button("Start New Game"):
        reset_game_state()

    # Display the game stats
    st.write("Guesses Remaining:", st.session_state.guesses_remaining)
    st.write("Questions Remaining:", st.session_state.questions_remaining)

    question_input = ""
    if st.session_state.questions_remaining > 0 and st.session_state.guesses_remaining > 0 :
        question_input = st.text_input("Ask a question to help you guess the animal")

    # handle the questions using the LLM
    if question_input:
        st.session_state.questions_remaining -= 1
        st.session_state.total_questions += 1
        answer = get_llm_response(question_input)
        st.session_state.question_history.append(question_input)
        st.session_state.answer_history.append(answer)
        st.write(answer)

    # User input for guessing the animal
    user_guess = st.text_input("What is your guess? (Type the animal name)", key="user_name_input")
    if user_guess:
        st.session_state.guesses_remaining -= 1
        # correct guess
        if user_guess.lower() == st.session_state.animal.lower():
            st.balloons()
            st.success("Yes, that's correct! Well done!", icon="🎉")
            st.session_state.won_game += 1
            st.session_state.guess_history.append(user_guess)
            st.session_state.guess_result_history.append("Yes")
        # incorrect guess
        if st.session_state.guesses_remaining > 0:
            st.write("No, that's not correct. Try again!")
            st.session_state.guess_history.append(user_guess)
            st.session_state.guess_result_history.append("No")

            # Button to get a hint about the animal
            if st.session_state.guesses_remaining == 1 and st.button("You wanna hint?"):
                hint = get_hint()
                st.write(hint)
        else:
            st.error("Sorry, you've run out of guesses! The correct answer was: " + st.session_state.animal)
            st.session_state.lost_game += 1
            st.session_state.guess_history.append(user_guess)
            st.session_state.guess_result_history.append("No")

    # Displaying the history of questions, answers, quessses and results
    st.write("### Question History")
    for question, answer in zip(st.session_state.question_history, st.session_state.answer_history):
        st.write(f"Q: {question} | A: {answer}")

    st.write("### Guess History")
    for guess, result in zip(st.session_state.guess_history, st.session_state.guess_result_history):
        st.write(f"Guess: {guess} | Result: {result}")


start_game()