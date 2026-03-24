import streamlit as st
from database import add_user, validate_user

def login():
    st.subheader("🔐 Login")

    username = st.text_input("Username", key="login_user")
    password = st.text_input("Password", type="password", key="login_pass")

    if st.button("Login"):
        if validate_user(username, password):
            st.session_state["user"] = username
            st.success("Login successful!")
        else:
            st.error("Invalid credentials")


def register():
    st.subheader("📝 Register")

    username = st.text_input("New Username", key="reg_user")
    password = st.text_input("New Password", type="password", key="reg_pass")

    if st.button("Register"):
        add_user(username, password)
        st.success("User registered successfully!")
