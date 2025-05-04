import streamlit as st
import random

# Initialize session state variables
if "player_score" not in st.session_state:
    st.session_state.player_score = 0
if "computer_score" not in st.session_state:
    st.session_state.computer_score = 0
if "game_message" not in st.session_state:
    st.session_state.game_message = ""
if "random_number" not in st.session_state:
    st.session_state.random_number = random.randint(0, 9)

st.title("🎲 Number Guessing Game (0 to 9)")
st.subheader("Can you beat the computer, Prem ji?")

# Input from user
user_input = st.number_input("Enter a number between 0 and 9", min_value=0, max_value=9, step=1)

if st.button("Submit Guess"):
    if user_input == st.session_state.random_number:
        st.session_state.player_score += 1
        st.session_state.game_message = "🎉 You won! Congratulations!"
    else:
        st.session_state.computer_score += 1
        st.session_state.game_message = (
            f"❌ Try again. Your number: {user_input}, Computer's number: {st.session_state.random_number}"
        )

    st.session_state.random_number = random.randint(0, 9)

# Display result message
if st.session_state.game_message:
    st.info(st.session_state.game_message)

# Show scores
st.write(f"**Score:** Player = {st.session_state.player_score}, Computer = {st.session_state.computer_score}")

# Reset option
if st.button("Reset Game"):
    st.session_state.player_score = 0
    st.session_state.computer_score = 0
    st.session_state.game_message = ""
    st.session_state.random_number = random.randint(0, 9)
    st.success("Game reset successfully!")

