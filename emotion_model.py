import pickle

def load_model():
    with open("emotion_model.pkl", "rb") as f:
        return pickle.load(f)

vectorizer, model = load_model()

def detect_emotion(text):
    vec = vectorizer.transform([text])
    return model.predict(vec)[0]