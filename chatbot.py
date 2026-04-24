import json
import random
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Load dataset
with open("intents.json") as file:
    data = json.load(file)

texts = []
labels = []

for intent in data["intents"]:
    for pattern in intent["patterns"]:
        texts.append(pattern)
        labels.append(intent["tag"])

# Vectorization (IMPORTANT upgrade)
vectorizer = TfidfVectorizer(ngram_range=(1,2), max_features=5000)
X = vectorizer.fit_transform(texts)

# Model
model = LogisticRegression(max_iter=200)
model.fit(X, labels)

def get_response(user_input):
    X_test = vectorizer.transform([user_input])
    
    probs = model.predict_proba(X_test)
    confidence = np.max(probs)

    tag = model.predict(X_test)[0]

    # 🔥 Smart fallback
    if confidence < 0.6:
        return "Samajh nahi aaya 😅, thoda aur clear likhoge?"

    for intent in data["intents"]:
        if intent["tag"] == tag:
            return random.choice(intent["responses"])

# Chat loop
print("🤖 Chatbot Ready! (type 'exit' to stop)\n")

while True:
    user = input("You: ")
    
    if user.lower() == "exit":
        print("Bot: Bye! 👋")
        break

    response = get_response(user)
    print("Bot:", response)
