import streamlit as st
from model import predict_intent, get_response

st.set_page_config(page_title="Smart Support Bot", page_icon="🤖")

st.title(" AI Customer Support Chatbot")

st.caption("Smart chatbot without API (offline logic)")


if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.chat_input("Ask anything...")

if user_input:
    # Use ML model for intent prediction
    tag = predict_intent(user_input)
    response = get_response(tag)

    st.session_state.chat_history.append(("user", user_input))
    st.session_state.chat_history.append(("bot", response))


for sender, message in st.session_state.chat_history:
    if sender == "user":
        st.chat_message("user").write(message)
    else:
        st.chat_message("assistant").write(message)
