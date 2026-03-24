# # 🌿 ECHO AI – Emotion-Centered Human Optimization

ECHO AI is a Streamlit-based web application that analyzes human emotions from text input and provides insights through dashboards and analytics.

It is designed as a lightweight, deployment-friendly AI project without heavy ML dependencies.

---

## 🚀 Features

- 🔐 User Registration & Login system  
- 🧠 Emotion detection (rule-based AI logic)  
- 📊 Interactive dashboard  
- 📈 Analytics with graphs (bar + pie charts)  
- 💬 Thought input analysis  
- 🗂️ User-specific emotion history  
- 🌐 Streamlit web interface (no frontend framework needed)

---

## 🧠 Concept

ECHO stands for:

> **Emotion-Centered Human Optimization**

The idea is to:
- Understand human emotions through text
- Track emotional patterns
- Provide insights to improve mental well-being

---

## 🖥️ Project Structure
ECHO_AI/ │── app.py │── auth.py │── database.py │── requirements.txt │ └── pages/ ├── 1_Register.py ├── 2_Login.py ├── 3_Dashboard.py ├── 4_Analytics.py

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/echo-ai.git
cd echo-ai

2. Install dependencies
Bash
pip install -r requirements.txt

3. Run app
Bash
streamlit run app.py

🌐 Deployment (Streamlit Cloud)
Push your project to GitHub
Go to https://share.streamlit.io⁠�
Connect your repository
Set:
Main file path → app.py
Click Deploy
🧾 Login Details (Demo)
Register a new user from the Register page, then login using:
Username: (your choice)
Password: (your choice)
🧪 How Emotion Detection Works
This project uses a rule-based NLP approach:
Keywords are matched from user input
Emotions classified into:
😊 Happy
😢 Sad
😡 Angry
😐 Neutral
Example:

Input: "I am very happy today"
Output: Happy
📊 Analytics
Bar chart → Emotion frequency
Pie chart → Emotion distribution
Helps visualize emotional trends
📸 Screenshots
Upload images in a /assets folder in your repo and reference them like below.
## 📸 Screenshots

### 🏠 Welcome Page
![Welcome](assets/welcome.jpg)

### 🔐 Login Page
![Login](assets/login.jpg)

### 📝 Register Page
![Register](assets/register.jpg)

### 📊 Dashboard
![Dashboard](assets/dashboard.jpg)

### 📈 Analytics
![Analytics](assets/analytics.jpg)

🧰 Tech Stack
Python 🐍
Streamlit ⚡
SQLite 🗄️
Pandas 📊
Matplotlib 📈

💡 Future Improvements
AI chatbot integration 🤖
Advanced ML/NLP model
Emotion trend prediction
Cloud database (Firebase / MongoDB)
Better UI/UX with animations

👨‍💻 Author
Deepak Dudeja

📄 License
This project is open-source and free to use for educational purposes.

