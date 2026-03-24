import streamlit as st
from database import init_db

st.set_page_config(page_title="ECHO AI", layout="wide")

# Initialize DB
init_db()

st.title("🌿 ECHO AI - Emotion-Centered Human Optimization")

st.sidebar.success("Navigate using pages below 👇")

st.markdown("""
## 🧠 About ECHO AI

ECHO (Emotion-Centered Human Optimization) is an AI-powered system designed to:

- Detect human emotions using NLP
- Store emotional history
- Provide personalized suggestions
- Help improve productivity and mental well-being

### 🚀 Features
- User authentication system
- Emotion detection
- Dashboard with insights
- Historical analysis
- Visualization of emotional trends

👉 Use the sidebar to explore the application.
""")
