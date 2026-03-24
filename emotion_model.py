import pickle

with open("emotion_model.pkl", "rb") as f:
    vectorizer, model = pickle.load(f)

def detect_emotion(text):
    vec = vectorizer.transform([text])
    return model.predict(vec)[0]