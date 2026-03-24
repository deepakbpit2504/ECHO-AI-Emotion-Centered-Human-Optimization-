import joblib

model = joblib.load("emotion_model.pkl")

def detect_emotion(text):
    prediction = model.predict([text])[0]
    return prediction