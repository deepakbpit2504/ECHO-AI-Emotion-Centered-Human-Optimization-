import streamlit as st
from database import init_db

st.set_page_config(page_title="ECHO AI", layout="wide")

init_db()

# Custom CSS for modern UI
st.markdown("""
<style>
body {
    background-color: #0f172a;
}

h1, h2, h3 {
    color: #38bdf8;
}

.card {
    background-color: #1e293b;
    padding: 20px;
    border-radius: 12px;
    margin-bottom: 15px;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.4);
}

.stButton>button {
    background-color: #38bdf8;
    color: white;
    border-radius: 8px;
}
</style>
""", unsafe_allow_html=True)

st.title("🌿 ECHO AI")
st.write("Emotion-Centered Human Optimization System")

st.sidebar.title("Navigation")
st.sidebar.info("Use the pages to navigate through the app")
