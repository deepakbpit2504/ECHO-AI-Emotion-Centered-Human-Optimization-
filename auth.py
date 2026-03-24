import streamlit as st
from database import add_user, validate_user

def login():
    st.markdown("## 🔐 Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if validate_user(username, password):
            st.session_state["user"] = username
            st.success("✅ Login successful")
        else:
            st.error("❌ Invalid credentials")


def register():
    st.markdown("## 📝 Register")

    username = st.text_input("New Username")
    password = st.text_input("New Password", type="password")

    if st.button("Register"):
        add_user(username, password)
        st.success("✅ User registered successfully")