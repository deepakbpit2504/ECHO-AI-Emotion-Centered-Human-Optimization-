import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from database import init_db, add_user, validate_user, save_emotion, get_emotions
from emotion_model import detect_emotion

st.set_page_config(page_title="ECHO AI", layout="wide")

init_db()

# Session state
if "page" not in st.session_state:
    st.session_state.page = "welcome"

if "user" not in st.session_state:
    st.session_state.user = None

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Navigation function
def go(page):
    st.session_state.page = page

# ---------------- WELCOME ----------------
if st.session_state.page == "welcome":
    st.title("🌿 ECHO AI")

    st.markdown("""
    ### 🧠 Emotion-Centered Human Optimization

    ECHO AI helps you:
    - Analyze emotions from text
    - Track mental patterns
    - Visualize emotional trends
    - Interact with an AI chatbot
    """)

    col1, col2 = st.columns(2)

    with col1:
        if st.button("📝 Register"):
            go("register")

    with col2:
        if st.button("🔐 Login"):
            go("login")

# ---------------- REGISTER ----------------
elif st.session_state.page == "register":
    st.title("📝 Register")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Register"):
        add_user(username, password)
        st.success("Registered successfully!")
        go("login")

    if st.button("⬅️ Back"):
        go("welcome")

# ---------------- LOGIN ----------------
elif st.session_state.page == "login":
    st.title("🔐 Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if validate_user(username, password):
            st.session_state.user = username
            go("dashboard")
        else:
            st.error("Invalid credentials")

    if st.button("⬅️ Back"):
        go("welcome")

# ---------------- DASHBOARD ----------------
elif st.session_state.page == "dashboard":
    if not st.session_state.user:
        go("login")
        st.stop()

    st.title("📊 Dashboard")
    st.write(f"Welcome 👋 {st.session_state.user}")

    # Emotion Analysis
    st.subheader("🧠 Enter Your Thoughts")

    text = st.text_area("Write something...")

    if st.button("Analyze Emotion"):
        emotion = detect_emotion(text)
        save_emotion(st.session_state.user, text, emotion)

        st.success(f"Detected Emotion: {emotion}")

    # Chatbot
    st.markdown("## 🤖 ECHO AI Chatbot")

    user_input = st.text_input("Ask something:")

    if st.button("Send"):
        response = ""

        if "stress" in user_input.lower():
            response = "Try breathing exercises and take short breaks."
        elif "sad" in user_input.lower():
            response = "It's okay to feel sad. Talk to someone you trust."
        elif "happy" in user_input.lower():
            response = "Great! Keep maintaining positivity 😊"
        else:
            response = "I'm here to help you understand your emotions."

        st.session_state.chat_history.append((user_input, response))

    for q, a in st.session_state.chat_history:
        st.markdown(f"**🧑 You:** {q}")
        st.markdown(f"**🤖 ECHO:** {a}")
        st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("📈 Analytics"):
            go("analytics")

    with col2:
        if st.button("🚪 Logout"):
            st.session_state.user = None
            go("welcome")

# ---------------- ANALYTICS ----------------
elif st.session_state.page == "analytics":
    if not st.session_state.user:
        go("login")
        st.stop()

    st.title("📈 Analytics Dashboard")

    data = get_emotions(st.session_state.user)

    if len(data) == 0:
        st.info("No data available")
    else:
        df = pd.DataFrame(data, columns=["Emotion"])

        st.subheader("📊 Emotion Distribution")

        counts = df["Emotion"].value_counts()

        st.bar_chart(counts)

        # Pie chart
        fig, ax = plt.subplots()
        ax.pie(counts, labels=counts.index, autopct='%1.1f%%')
        ax.set_title("Emotion Distribution")
        st.pyplot(fig)

        # Emotional score
        score_map = {
            "Happy": 2,
            "Angry": -1,
            "Sad": -2
        }

        scores = df["Emotion"].map(score_map)
        avg_score = scores.mean()

        st.metric("🧠 Emotional Score", round(avg_score, 2))

    if st.button("⬅️ Back"):
        go("dashboard")