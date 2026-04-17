import streamlit as st
from model import predict_intent, get_response
from datetime import datetime
import model  # ensures training

st.set_page_config(page_title="Support Bot", page_icon="🤖")

st.title("🤖 Customer Support Chatbot")
st.caption("AI-powered chatbot using NLP & Machine Learning")

# Chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Input
user_input = st.chat_input("Type your message...")

if user_input:
    tag = predict_intent(user_input)

    # Special handling for time
    if tag == "time":
        response = f"Current time is {datetime.now().strftime('%H:%M:%S')}"
    else:
        response = get_response(tag)

    st.session_state.chat_history.append(("user", user_input))
    st.session_state.chat_history.append(("bot", response))

# Display chat
for sender, message in st.session_state.chat_history:
    if sender == "user":
        st.chat_message("user").write(message)
    else:
        st.chat_message("assistant").write(message)
