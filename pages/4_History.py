import streamlit as st
import pandas as pd
from database import get_emotions

st.title("📈 Emotion History")

if "user" not in st.session_state:
    st.warning("⚠️ Please login first")
    st.stop()

user = st.session_state["user"]

data = get_emotions(user)

if len(data) == 0:
    st.info("No history available 📭")
else:
    df = pd.DataFrame(data, columns=["Text", "Emotion"])

    st.dataframe(df, use_container_width=True)

    st.subheader("📊 Emotion Distribution")
    st.bar_chart(df["Emotion"].value_counts())

    st.markdown("""
    <div class="card">
    <h3>🧾 Insight</h3>
    <p>This visualization helps you understand your emotional trends over time.</p>
    </div>
    """, unsafe_allow_html=True)