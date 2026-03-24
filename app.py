import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from database import init_db, add_user, validate_user, save_emotion, get_emotions
from emotion_model import detect_emotion

# ---------------- CONFIG ----------------
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

# ---------------- STYLE ----------------
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
    <h2>🧠 Emotion-Centered Human Optimization (ECHO)</h2>

    <p>
    ECHO AI is an intelligent system that uses Machine Learning and Natural Language Processing
    to analyze human emotions from text input and provide meaningful insights.
    </p>

    <hr>

    <h3>📘 What is ECHO?</h3>
    <p>
    ECHO stands for Emotion-Centered Human Optimization. It focuses on understanding emotional patterns
    and improving mental awareness using AI techniques.
    </p>

    <h3>🎯 Why Use ECHO?</h3>
    <ul>
        <li>Understand your emotional patterns</li>
        <li>Improve mental well-being</li>
        <li>Track mood over time</li>
        <li>Gain AI-driven insights</li>
    </ul>

    <h3>⚙️ How It Works</h3>
    <ul>
        <li>User inputs text</li>
        <li>ML model processes the text</li>
        <li>Emotion is predicted (Happy, Sad, Angry, etc.)</li>
        <li>Data is stored and visualized</li>
    </ul>

    <h3>🤖 Technologies Used</h3>
    <ul>
        <li>Machine Learning (Logistic Regression)</li>
        <li>TF-IDF Vectorization</li>
        <li>Streamlit Web App</li>
        <li>SQLite Database</li>
    </ul>

    <p style="color:#38bdf8;">
    🚀 Start by registering or logging in to explore your emotions.
    </p>
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
    <h3>📘 Why Register?</h3>
    <ul>
        <li>Create a personal account</li>
        <li>Store your emotional data</li>
        <li>Enable analytics tracking</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Register"):
        add_user(username, password)
        st.success("Registered successfully!")
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
        <li>Protected emotional history</li>
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
            st.error("Invalid credentials")

    if st.button("⬅️ Back"):
        go("welcome")

# ================= DASHBOARD =================
elif st.session_state.page == "dashboard":
    if not st.session_state.user:
        go("login")
        st.stop()

    st.title("📊 Dashboard")

    st.markdown("""
    <div class="card">
    <h3>📘 Dashboard Overview</h3>
    <ul>
        <li>Enter your thoughts for emotion analysis</li>
        <li>AI model predicts emotion</li>
        <li>Data stored for analytics</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

    text = st.text_area("Enter your thought")

    if st.button("Analyze Emotion"):
        if text.strip():
            emotion = detect_emotion(text)
            save_emotion(st.session_state.user, text, emotion)
            st.success(f"Detected Emotion: {emotion}")

    # -------- CHATBOT --------
    st.markdown("## 🤖 Chatbot")

    user_input = st.text_input("Ask something")

    if st.button("Send"):
        if "stress" in user_input.lower():
            response = "Try relaxation techniques and deep breathing."
        elif "sad" in user_input.lower():
            response = "Stay strong. Talk to someone you trust."
        elif "happy" in user_input.lower():
            response = "Great! Keep going 😊"
        else:
            response = "I'm here to help you understand emotions."

        st.session_state.chat_history.append((user_input, response))

    for q, a in st.session_state.chat_history:
        st.write("🧑", q)
        st.write("🤖", a)
        st.write("---")

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
        <li>Bar chart shows emotion frequency</li>
        <li>Pie chart shows distribution</li>
        <li>Score indicates overall mood</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

    data = get_emotions(st.session_state.user)

    if len(data) == 0:
        st.info("No data available")
    else:
        df = pd.DataFrame(data, columns=["Emotion"])

        counts = df["Emotion"].value_counts()

        st.subheader("📊 Emotion Distribution")
        st.bar_chart(counts)

        fig, ax = plt.subplots()
        ax.pie(counts, labels=counts.index, autopct='%1.1f%%')
        st.pyplot(fig)

        score_map = {"Happy": 2, "Angry": -1, "Sad": -2}
        scores = df["Emotion"].map(score_map)
        avg_score = scores.mean()

        st.subheader("🧠 Emotional Score")
        st.metric("Average Mood Score", round(avg_score, 2))

    if st.button("⬅️ Back"):
        go("dashboard")