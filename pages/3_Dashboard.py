import streamlit as st
from emotion_model import detect_emotion
from database import save_emotion

st.title("📊 Dashboard")

if "user" not in st.session_state:
    st.warning("Please login first")
    st.stop()

user = st.session_state["user"]

st.write(f"Welcome **{user}** 👋")

text = st.text_area("Enter your thoughts:")

if st.button("Analyze Emotion"):
    emotion = detect_emotion(text)

    save_emotion(user, text, emotion)

    st.success(f"Detected Emotion: {emotion}")

    # Recommendation Engine (Rule-based AI logic)
    if "Sad" in emotion:
        st.info("💡 Suggestion: Take a break, talk to a friend, or meditate.")
    elif "Happy" in emotion:
        st.info("💡 Suggestion: Maintain your positive habits!")
    else:
        st.info("💡 Suggestion: Stay balanced and focused.")
