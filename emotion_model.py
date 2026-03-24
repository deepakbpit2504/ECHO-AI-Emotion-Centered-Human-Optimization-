from textblob import TextBlob

def detect_emotion(text):
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity

    # Advanced rule-based classification
    if polarity > 0.5:
        return "Very Happy"
    elif polarity > 0.1:
        return "Happy"
    elif polarity < -0.5:
        return "Very Sad"
    elif polarity < -0.1:
        return "Sad"
    else:
        return "Neutral"
