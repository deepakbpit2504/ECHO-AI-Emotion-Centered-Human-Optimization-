import streamlit as st
import pandas as pd
from database import get_emotions

st.title("📈 Emotion History")

if "user" not in st.session_state:
    st.warning("Please login first")
    st.stop()

user = st.session_state["user"]

data = get_emotions(user)

if len(data) == 0:
    st.info("No history available.")
else:
    df = pd.DataFrame(data, columns=["Text", "Emotion"])

    st.dataframe(df)

    st.subheader("Emotion Distribution")

    st.bar_chart(df["Emotion"].value_counts())
