import streamlit as st
from emotion_model import detect_emotion
from database import save_emotion

st.title("📊 Dashboard")

if "user" not in st.session_state:
    st.warning("⚠️ Please login first")
    st.stop()

user = st.session_state["user"]

st.markdown(f"### 👋 Welcome, **{user}**")

text = st.text_area("✍️ Enter your thoughts")

if st.button("🧠 Analyze Emotion"):
    emotion = detect_emotion(text)
    save_emotion(user, text, emotion)

    st.markdown(f"""
    <div class="card">
    <h3>🎯 Emotion Detected: {emotion}</h3>
    </div>
    """, unsafe_allow_html=True)

    if "Sad" in emotion:
        st.info("💡 Suggestion: Take rest, listen to music 🎧 or talk to someone.")
    elif "Happy" in emotion:
        st.success("💡 Keep maintaining your positive mindset! 😊")
    else:
        st.warning("💡 Stay balanced ⚖️")