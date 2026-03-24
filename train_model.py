import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import joblib

# Sample dataset (expand later for better accuracy)
data = {
    "text": [
        "I am very happy today",
        "This is amazing",
        "I feel sad and lonely",
        "I am very stressed",
        "I am excited",
        "I feel terrible",
        "I love this",
        "This is bad",
        "I am depressed",
        "I feel great",
        "I am anxious",
        "I am angry"
    ],
    "emotion": [
        "Happy",
        "Happy",
        "Sad",
        "Sad",
        "Happy",
        "Sad",
        "Happy",
        "Sad",
        "Sad",
        "Happy",
        "Sad",
        "Angry"
    ]
}

df = pd.DataFrame(data)

X_train, X_test, y_train, y_test = train_test_split(
    df["text"], df["emotion"], test_size=0.2, random_state=42
)

model = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("clf", LogisticRegression(max_iter=200))
])

model.fit(X_train, y_train)

joblib.dump(model, "emotion_model.pkl")

print("✅ Model trained and saved as emotion_model.pkl")