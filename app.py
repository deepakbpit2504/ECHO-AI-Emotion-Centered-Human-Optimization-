import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from database import init_db, add_user, validate_user, save_emotion, get_emotions
from emotion_model import detect_emotion

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="ECHO AI", layout="wide")

init_db()

# ---------------- SESSION STATE ----------------
if "page" not in st.session_state:
    st.session_state.page = "welcome"

if "user" not in st.session_state:
    st.session_state.user = None

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

def go(page):
    st.session_state.page = page

# ---------------- UI STYLE ----------------
st.markdown("""
<style>
.card {
    background-color: #0f172a;
    padding: 20px;
    border-radius: 12px;
    margin-bottom: 15px;
}
.title {
    font-size: 40px;
    font-weight: bold;
    color: #38bdf8;
}
</style>
""", unsafe_allow_html=True)

# ================= WELCOME =================
if st.session_state.page == "welcome":
    st.markdown('<div class="title">🌿 ECHO AI</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
    <h3>🧠 Emotion-Centered Human Optimization (ECHO)</h3>
    <p>
    ECHO AI is an AI-powered system designed to help users understand, analyze,
    and improve their emotional well-being using Machine Learning.
    </p>

    <h4>🎯 Purpose:</h4>
    <ul>
        <li>Analyze emotions from text input</li>
        <li>Track emotional patterns over time</li>
        <li>Provide insights through analytics</li>
        <li>Assist users via AI chatbot</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        if st.button("📝 Register"):
            go("register")

    with col2:
        if st.button("🔐 Login"):
            go("login")

# ================= REGISTER =================
elif st.session_state.page == "register":
    st.title("📝 Register")

    st.markdown("""
    <div class="card">
    <h3>📘 Why Registration?</h3>
    <ul>
        <li>Create a personal account</li>
        <li>Store your emotional history</li>
        <li>Enable personalized analytics</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Register"):
        add_user(username, password)
        st.success("✅ Registered successfully!")
        go("login")

    if st.button("⬅️ Back"):
        go("welcome")

# ================= LOGIN =================
elif st.session_state.page == "login":
    st.title("🔐 Login")

    st.markdown("""
    <div class="card">
    <h3>📘 Why Login?</h3>
    <ul>
        <li>Secure access to your data</li>
        <li>Personalized dashboard</li>
        <li>Private emotion tracking</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if validate_user(username, password):
            st.session_state.user = username
            go("dashboard")
        else:
            st.error("❌ Invalid credentials")

    if st.button("⬅️ Back"):
        go("welcome")

# ================= DASHBOARD =================
elif st.session_state.page == "dashboard":
    if not st.session_state.user:
        go("login")
        st.stop()

    st.title("📊 Dashboard")
    st.write(f"👋 Welcome **{st.session_state.user}**")

    st.markdown("""
    <div class="card">
    <h3>📘 Dashboard Overview</h3>
    <ul>
        <li>Enter your thoughts to analyze emotions</li>
        <li>AI model predicts emotional state</li>
        <li>Results are stored for analytics</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

    # -------- Emotion Input --------
    st.subheader("🧠 Analyze Your Thoughts")

    text = st.text_area("Enter your thought:")

    if st.button("Analyze Emotion"):
        if text.strip() != "":
            emotion = detect_emotion(text)
            save_emotion(st.session_state.user, text, emotion)

            st.success(f"Detected Emotion: **{emotion}**")
        else:
            st.warning("Please enter some text.")

    # -------- Chatbot --------
    st.markdown("## 🤖 ECHO AI Chatbot")

    st.markdown("""
    <div class="card">
    <h4>💬 Chatbot Info</h4>
    <p>
    The chatbot provides supportive responses based on your input.
    It helps guide users with emotional awareness and suggestions.
    </p>
    </div>
    """, unsafe_allow_html=True)

    user_input = st.text_input("Ask something:")

    if st.button("Send"):
        response = ""

        if "stress" in user_input.lower():
            response = "Try deep breathing and take short breaks."
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

# ================= ANALYTICS =================
elif st.session_state.page == "analytics":
    if not st.session_state.user:
        go("login")
        st.stop()

    st.title("📈 Analytics Dashboard")

    st.markdown("""
    <div class="card">
    <h3>📘 Analytics Explanation</h3>
    <ul>
        <li>Bar chart shows frequency of emotions</li>
        <li>Pie chart shows percentage distribution</li>
        <li>Emotional score represents overall mood trend</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

    data = get_emotions(st.session_state.user)

    if len(data) == 0:
        st.info("No data available yet.")
    else:
        df = pd.DataFrame(data, columns=["Emotion"])

        counts = df["Emotion"].value_counts()

        st.subheader("📊 Emotion Distribution")
        st.bar_chart(counts)

        # Pie chart
        fig, ax = plt.subplots()
        ax.pie(counts, labels=counts.index, autopct='%1.1f%%')
        ax.set_title("Emotion Distribution")
        st.pyplot(fig)

        # Emotional Score
        score_map = {
            "Happy": 2,
            "Angry": -1,
            "Sad": -2
        }

        scores = df["Emotion"].map(score_map)
        avg_score = scores.mean()

        st.subheader("🧠 Emotional Score")
        st.metric("Average Mood Score", round(avg_score, 2))

    if st.button("⬅️ Back to Dashboard"):
        go("dashboard")