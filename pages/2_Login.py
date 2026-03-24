import streamlit as st
from database import validate_user

st.title("🔐 Login")

st.markdown("""
### 📘 Login Theory

Login is used to verify user identity before accessing the system.

It ensures:
- Security
- Data privacy
- Personalized dashboard access
""")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if "user" not in st.session_state:
    st.session_state.user = None

if st.button("Login"):
    if validate_user(username, password):
        st.session_state.user = username
        st.success("Login successful!")
    else:
        st.error("Invalid credentials")