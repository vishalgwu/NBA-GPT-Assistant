import streamlit as st
import requests
import datetime

API_URL = "https://g0m0e9kp77.execute-api.us-east-1.amazonaws.com/prod/ask"


# -----------------------------
# Make page beautiful
# -----------------------------
st.set_page_config(page_title="NBA GPT", page_icon="🏀", layout="centered")

st.markdown(
    """
    <style>
    body {
        background-color: #0d0d0d;
    }
    .main {
        background-color: #0d0d0d;
        color: white;
    }
    .chat-bubble-user {
        background-color: #1e1e1e;
        padding: 10px 15px;
        border-radius: 12px;
        margin-bottom: 8px;
        width: fit-content;
        max-width: 80%;
    }
    .chat-bubble-bot {
        background-color: #00335c;
        padding: 10px 15px;
        border-radius: 12px;
        margin-bottom: 8px;
        width: fit-content;
        max-width: 80%;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# -----------------------------
# Title & description
# -----------------------------
st.title("🏀 NBA GPT Assistant")
st.write("Ask anything about NBA players, games, stats, history, and more!")


# Initialize chat history
if "history" not in st.session_state:
    st.session_state.history = []


# -----------------------------
# Function to call API Gateway
# -----------------------------
def ask_api(question):
    payload = {"question": question}

    try:
        response = requests.post(API_URL, json=payload, timeout=20)
        response.raise_for_status()

        data = response.json()
        return data.get("answer", "No answer received.")
    except Exception as e:
        return f"⚠️ API Error: {str(e)}"


# -----------------------------
# USER INPUT
# -----------------------------
user_input = st.text_input("Your Question:", placeholder="e.g., Tell me about Stephen Curry")

if st.button("Ask"):
    if user_input.strip() == "":
        st.warning("Please enter a question.")
    else:
        # Add user message to history
        st.session_state.history.append({
            "role": "user",
            "content": user_input,
            "time": datetime.datetime.now().strftime("%H:%M")
        })

        with st.spinner("Thinking... 🤖"):
            answer = ask_api(user_input)

        # Add bot answer
        st.session_state.history.append({
            "role": "bot",
            "content": answer,
            "time": datetime.datetime.now().strftime("%H:%M")
        })


# -----------------------------
# DISPLAY CHAT HISTORY
# -----------------------------
st.write("### 💬 Chat History")

for msg in st.session_state.history:
    if msg["role"] == "user":
        st.markdown(
            f"<div class='chat-bubble-user'>👤 <b>You</b> ({msg['time']}):<br>{msg['content']}</div>",
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            f"<div class='chat-bubble-bot'>🤖 <b>NBA GPT</b> ({msg['time']}):<br>{msg['content']}</div>",
            unsafe_allow_html=True
        )

