import streamlit as st
from openai import OpenAI
from datetime import datetime

# 🔑 Add your API key here
client = OpenAI(api_key="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")

st.set_page_config(page_title="Smart Support Bot", page_icon="🤖")

st.title("🤖 AI Customer Support Chatbot")


# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Input
user_input = st.chat_input("Ask anything...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    # 🔥 GPT Response
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=st.session_state.messages
    )

    bot_reply = response.choices[0].message.content

    st.session_state.messages.append({"role": "assistant", "content": bot_reply})

# Display chat
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.chat_message("user").write(msg["content"])
    else:
        st.chat_message("assistant").write(msg["content"])
