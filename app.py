import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Smart Support Bot", page_icon="🤖")

st.title(" AI Customer Support Chatbot")

st.caption("Smart chatbot without API (offline logic)")


if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.chat_input("Ask anything...")

def smart_reply(text):
    text = text.lower()

   
    if any(word in text for word in ["hi", "hello", "hey"]):
        return "Hello! How can I assist you today?"

    
    if "refund" in text:
        return "Sure, I can help with refunds. Please provide your order ID."

    
    if any(word in text for word in ["order", "delivery", "track"]):
        return "You can track your order using your order ID. Please share it."

   
    if "time" in text:
        return f"Current time is {datetime.now().strftime('%H:%M:%S')}"

   
    if "your name" in text or "who are you" in text:
        return "I am your AI customer support assistant."

    
    if "how are you" in text:
        return "I'm doing great! How can I help you?"

    
    return "That's an interesting question! I can help with orders, refunds, tracking, or general queries."


if user_input:
    response = smart_reply(user_input)

    st.session_state.chat_history.append(("user", user_input))
    st.session_state.chat_history.append(("bot", response))


for sender, message in st.session_state.chat_history:
    if sender == "user":
        st.chat_message("user").write(message)
    else:
        st.chat_message("assistant").write(message)

print("Test by Pratyush")
