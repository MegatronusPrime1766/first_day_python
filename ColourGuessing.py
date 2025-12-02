import streamlit as st
import random

st.title("🎨 Simple Color Guessing Game")

colors = ["red", "green", "blue", "yellow", "purple", "orange"]

# Pick a random color
secret_color = random.choice(colors)

st.write("I'm thinking of one of these colors:")
st.write(", ".join(colors))

guess = st.text_input("Your guess:")

if st.button("Check"):
    if guess.lower() == secret_color:
        st.success(f"🎉 Correct! The color was **{secret_color}**")
    else:
        st.error(f"❌ Nope! The color was **{secret_color}**")

st.write("Reload the page to play again!")
