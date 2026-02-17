import streamlit as st
import requests
import json

# --- 1. CONFIGURATION ---
API_URL = "http://127.0.0.1:8000/query"
st.set_page_config(page_title="Agentic RAG", page_icon="🤖", layout="centered")

# --- 2. CUSTOM CSS FOR AESTHETICS ---
# This applies a dark theme, rounded corners, and a glowing effect
st.markdown("""
<style>
    /* Main Background */
    .stApp {
        background: linear-gradient(to bottom right, #0e1117, #161b22);
        color: #ffffff;
    }
    
    /* Header Style */
    .main-header {
        font-size: 2.5rem;
        font-weight: 700;
        background: -webkit-linear-gradient(45deg, #00C9FF, #92FE9D);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 2rem;
    }

    /* Chat Message Bubbles */
    .stChatMessage {
        background-color: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 15px;
        padding: 10px;
        transition: transform 0.2s;
    }
    .stChatMessage:hover {
        background-color: rgba(255, 255, 255, 0.08);
        transform: scale(1.01);
    }

    /* Input Box Styling */
    .stTextInput > div > div > input {
        background-color: rgba(255, 255, 255, 0.05);
        color: white;
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.2);
    }
    
    /* Hide Default Streamlit Elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# --- 3. SESSION STATE (MEMORY) ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# --- 4. HEADER ---
st.markdown('<div class="main-header">🤖 Agentic RAG Chat</div>', unsafe_allow_html=True)
st.markdown("<div style='text-align: center; color: #8b949e; margin-bottom: 30px;'>Ask questions about your PDF documents with AI reasoning.</div>", unsafe_allow_html=True)

# --- 5. DISPLAY CHAT HISTORY ---
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- 6. CHAT INPUT & LOGIC ---
if prompt := st.chat_input("Type your question here..."):
    # 1. Display User Message
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # 2. Show a cool spinner while thinking
    with st.spinner("🧠 Agent is thinking..."):
        try:
            # Send to backend API
            payload = {"question": prompt}
            response = requests.post(API_URL, json=payload)
            
            if response.status_code == 200:
                answer = response.json().get("answer", "No answer found.")
                
                # Display Bot Message
                with st.chat_message("assistant"):
                    st.markdown(answer)
                
                # Save to history
                st.session_state.messages.append({"role": "assistant", "content": answer})
            else:
                st.error(f"API Error: {response.status_code}")
        
        except requests.exceptions.ConnectionError:
            st.error("❌ Could not connect to the API. Is `main.py` running?")