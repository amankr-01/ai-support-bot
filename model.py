import json
import random
import pickle
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Load intents
with open("intents.json") as file:
    data = json.load(file)

# Train only if model not exists
if not os.path.exists("model.pkl"):

    texts = []
    labels = []

    for intent in data["intents"]:
        for pattern in intent["patterns"]:
            texts.append(pattern.lower())
            labels.append(intent["tag"])

    # Improved vectorizer
    vectorizer = TfidfVectorizer(
        ngram_range=(1, 2),
        stop_words='english'
    )

    X = vectorizer.fit_transform(texts)

    model = LogisticRegression(max_iter=200)
    model.fit(X, labels)

    pickle.dump(model, open("model.pkl", "wb"))
    pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))

# Prediction function
def predict_intent(text):
    model = pickle.load(open("model.pkl", "rb"))
    vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

    X_test = vectorizer.transform([text.lower()])
    
    probs = model.predict_proba(X_test)
    confidence = max(probs[0])

    if confidence < 0.6:
        return "unknown"

    return model.predict(X_test)[0]

# Response function
def get_response(tag):
    if tag == "unknown":
        return random.choice([
            "I'm not sure I understood that. Can you rephrase?",
            "Could you please clarify your request?",
            "I didn't get that. Try asking about orders or refunds."
        ])

    for intent in data["intents"]:
        if intent["tag"] == tag:
            return random.choice(intent["responses"])
