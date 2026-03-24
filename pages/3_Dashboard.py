import streamlit as st
from database import save_emotion

st.title("📊 Dashboard")

st.markdown("""
### 📘 Dashboard Theory

This dashboard allows users to:
- Enter thoughts
- Analyze emotions
- Store results for analytics

The emotion detection uses rule-based AI logic (keyword matching).
""")

if "user" not in st.session_state or st.session_state.user is None:
    st.warning("Please login first")
    st.stop()

def detect_emotion(text):
    text = text.lower()

    if any(word in text for word in ["happy", "great", "love", "amazing", "good"]):
        return "Happy"
    elif any(word in text for word in ["sad", "bad", "depressed", "lonely"]):
        return "Sad"
    elif any(word in text for word in ["angry", "hate", "frustrated", "annoyed"]):
        return "Angry"
    else:
        return "Neutral"

text = st.text_area("Enter your thought")

if st.button("Analyze"):
    if text:
        emotion = detect_emotion(text)
        save_emotion(st.session_state.user, text, emotion)
        st.success(f"Detected Emotion: {emotion}")