import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from database import get_emotions

st.title("📈 Analytics")

st.markdown("""
### 📘 Analytics Theory

This section visualizes emotional trends:
- Bar chart shows frequency
- Pie chart shows distribution
- Helps understand emotional patterns
""")

if "user" not in st.session_state or st.session_state.user is None:
    st.warning("Please login first")
    st.stop()

data = get_emotions(st.session_state.user)

if len(data) == 0:
    st.info("No data available")
else:
    df = pd.DataFrame(data, columns=["Emotion"])
    counts = df["Emotion"].value_counts()

    st.bar_chart(counts)

    fig, ax = plt.subplots()
    ax.pie(counts, labels=counts.index, autopct="%1.1f%%")
    st.pyplot(fig)