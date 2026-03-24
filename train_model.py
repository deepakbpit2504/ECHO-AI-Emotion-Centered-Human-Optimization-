import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

texts = [
    "I am happy", "I feel great", "This is amazing",
    "I am sad", "I feel bad", "This is terrible",
    "I am angry", "I hate this", "I love this",
    "What a wonderful day"
]

labels = [
    "Happy", "Happy", "Happy",
    "Sad", "Sad", "Sad",
    "Angry", "Angry", "Happy",
    "Happy"
]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(texts)

model = LogisticRegression()
model.fit(X, labels)

with open("emotion_model.pkl", "wb") as f:
    pickle.dump((vectorizer, model), f)

print("Model saved!")