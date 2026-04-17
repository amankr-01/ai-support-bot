import streamlit as st
from model import predict_intent, get_response
import model  # ensures model training runs

st.set_page_config(page_title="Support Bot", page_icon="🤖")

st.title("🤖 Customer Support Chatbot")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("Type your message...")

if st.button("Send"):
    if user_input:
        tag = predict_intent(user_input)
        response = get_response(tag)

        st.session_state.chat_history.append(("You", user_input))
        st.session_state.chat_history.append(("Bot", response))

# Display chat
for sender, message in st.session_state.chat_history:
    st.write(f"**{sender}:** {message}")
