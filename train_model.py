import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Training data
texts = [
    "I am happy", "I feel great", "I love this", "Amazing day",
    "I am sad", "I feel bad", "Very depressing",
    "I am angry", "I hate this", "This is frustrating"
]

labels = [
    "Happy", "Happy", "Happy", "Happy",
    "Sad", "Sad", "Sad",
    "Angry", "Angry", "Angry"
]

# Vectorization
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(texts)

# Train model
model = LogisticRegression()
model.fit(X, labels)

# Save model
with open("emotion_model.pkl", "wb") as f:
    pickle.dump((vectorizer, model), f)

print("✅ emotion_model.pkl created successfully!")