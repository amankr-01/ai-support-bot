import json
import random
import pickle
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression


with open("intents.json") as file:
    data = json.load(file)


if not os.path.exists("model.pkl"):

    texts = []
    labels = []

    for intent in data["intents"]:
        for pattern in intent["patterns"]:
            texts.append(pattern.lower())
            labels.append(intent["tag"])

    
    vectorizer = TfidfVectorizer(
        ngram_range=(1, 2),
        stop_words='english'
    )

    X = vectorizer.fit_transform(texts)

    model = LogisticRegression(max_iter=200)
    model.fit(X, labels)

    pickle.dump(model, open("model.pkl", "wb"))
    pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))



def predict_intent(text):
    model = pickle.load(open("model.pkl", "rb"))
    vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

    X_test = vectorizer.transform([text.lower()])
    probs = model.predict_proba(X_test)
    confidence = max(probs[0])

    # Lowered threshold for more flexibility
    if confidence < 0.45:
        return "unknown"

    return model.predict(X_test)[0]


import datetime

def get_response(tag):
    if tag == "unknown":
        return random.choice([
            "I'm not sure I understood that. Can you rephrase?",
            "Could you please clarify your request?",
            "I didn't get that. Try asking about orders, refunds, time, or date."
        ])
    if tag == "time":
        now = datetime.datetime.now().strftime("%H:%M:%S")
        return f"Current time is {now}"
    if tag == "date":
        today = datetime.datetime.now().strftime("%Y-%m-%d")
        return f"Today's date is {today}"
    for intent in data["intents"]:
        if intent["tag"] == tag:
            return random.choice(intent["responses"])

    for intent in data["intents"]:
        if intent["tag"] == tag:
            return random.choice(intent["responses"])
