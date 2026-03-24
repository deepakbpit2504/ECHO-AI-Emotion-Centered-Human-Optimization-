import streamlit as st
from database import add_user

st.title("📝 Register")

st.markdown("""
### 📘 Registration Theory

Registration allows users to create an account in the system.

It helps:
- Store personal data
- Enable login authentication
- Maintain user-specific emotion history
""")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Register"):
    add_user(username, password)
    st.success("Registered successfully!")