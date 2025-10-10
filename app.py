import streamlit as st
from textblob import TextBlob

# List of inappropriate words to filter
bad_words = ['badword1', 'badword2']

def safe_text(text):
    for word in bad_words:
        if word in text.lower():
            return False
    return True

def get_mood(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0.2:
        return "😀", "Sounds happy!"
    elif polarity < -0.2:
        return "😞", "Feels sad!"
    else:
        return "😐", "Neutral mood."

st.title("Kid-safe Text-Mood Detector")

sentence = st.text_input("Enter a sentence:")

if st.button("Detect Mood"):
    if sentence.strip() == "":
        st.write("Please enter a sentence.")
    elif safe_text(sentence):
        emoji, explanation = get_mood(sentence)
        st.write(f"Result: {emoji} — {explanation}")
    else:
        st.write("😐 — Inappropriate language detected.")

# Optional Teacher Mode (simple explanation)
if st.checkbox("Teacher Mode"):
    st.write("This app analyzes the mood of the sentence using simple sentiment polarity:")
    st.write(" - Positive polarity → 😀 Happy")
    st.write(" - Negative polarity → 😞 Sad")
    st.write(" - Neutral polarity → 😐 Neutral")
