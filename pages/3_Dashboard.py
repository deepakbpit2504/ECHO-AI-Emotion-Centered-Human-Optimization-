import streamlit as st
from emotion_model import detect_emotion
from database import save_emotion

st.title("📊 Dashboard")

st.markdown("""
### 📘 Dashboard Overview

The dashboard is the main working area of ECHO AI.

**Features:**
- Input your thoughts or text
- AI model analyzes emotion
- Results are stored for future insights

**Working:**
- User enters a sentence
- Machine Learning model processes it
- Emotion is predicted (Happy, Sad, Angry, etc.)
- Data is saved in the database
""")

if "user" not in st.session_state or st.session_state.user is None:
    st.warning("Please login first")
    st.stop()

text = st.text_area("Enter your thought")

if st.button("Analyze"):
    if text:
        emotion = detect_emotion(text)
        save_emotion(st.session_state.user, text, emotion)
        st.success(f"Detected Emotion: {emotion}")