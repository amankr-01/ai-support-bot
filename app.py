import streamlit as st
from model import predict_intent, get_response
from datetime import datetime
import model

st.set_page_config(page_title="Support Bot", page_icon="🤖")

st.title("🤖 Customer Support Chatbot")
st.caption("AI-powered chatbot using NLP & Machine Learning")

# Chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Input
user_input = st.chat_input("Type your message...")

if user_input:
    tag = predict_intent(user_input.lower())

    # 🎯 Known intents
    if tag == "time":
        response = f"Current time is {datetime.now().strftime('%H:%M:%S')}"
    elif tag != "unknown":
        response = get_response(tag)

    # 🧠 Smart fallback (NO AI garbage)
    else:
        text = user_input.lower()

        if "how are you" in text:
            response = "I'm doing great! How can I assist you today?"
        elif "your name" in text or "who are you" in text:
            response = "I'm your AI customer support assistant."
        elif "help" in text:
            response = "I can help you with orders, refunds, tracking, and general queries."
        elif "time" in text:
            response = f"Current time is {datetime.now().strftime('%H:%M:%S')}"
        else:
            response = "Sorry, I didn't understand that. You can ask about orders, refunds, or general questions."

    st.session_state.chat_history.append(("user", user_input))
    st.session_state.chat_history.append(("bot", response))

# Display chat
for sender, message in st.session_state.chat_history:
    if sender == "user":
        st.chat_message("user").write(message)
    else:
        st.chat_message("assistant").write(message)
