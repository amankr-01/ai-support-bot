import streamlit as st
from model import predict_intent, get_response
from datetime import datetime
from transformers import pipeline
import model

st.set_page_config(page_title="Support Bot", page_icon="🤖")

st.title("🤖 Smart Customer Support Chatbot")
st.caption("Now powered with AI fallback 🔥")

# Load AI model (only once)
@st.cache_resource
def load_ai():
    return pipeline("text-generation", model="distilgpt2")

ai_model = load_ai()

# Chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Input
user_input = st.chat_input("Type your message...")

if user_input:
    tag = predict_intent(user_input)

    # 🎯 If known intent → use your ML bot
    if tag != "unknown":
        if tag == "time":
            response = f"Current time is {datetime.now().strftime('%H:%M:%S')}"
        else:
            response = get_response(tag)

    # 🧠 If unknown → use AI (SMART RESPONSE)
    else:
        ai_response = ai_model(user_input, max_length=50, num_return_sequences=1)
        response = ai_response[0]["generated_text"]

    st.session_state.chat_history.append(("user", user_input))
    st.session_state.chat_history.append(("bot", response))

# Display chat
for sender, message in st.session_state.chat_history:
    if sender == "user":
        st.chat_message("user").write(message)
    else:
        st.chat_message("assistant").write(message)
