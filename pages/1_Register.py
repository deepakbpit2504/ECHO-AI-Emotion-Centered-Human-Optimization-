import streamlit as st
from database import add_user

st.title("📝 Register")

st.markdown("""
### 📘 Why Registration?

Registration allows users to create a personal account in the ECHO AI system.

**Purpose:**
- Store user-specific emotional data
- Enable personalized analytics
- Maintain secure access to the system

**How it works:**
- User enters username and password
- Credentials are stored in a database
- User can later login using the same credentials
""")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Register"):
    add_user(username, password)
    st.success("Registered successfully!")