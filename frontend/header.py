import streamlit as st


def show_header():

    st.markdown("""
    <div style="
        background: linear-gradient(90deg,#1E3A8A,#2563EB);
        padding:25px;
        border-radius:15px;
        text-align:center;
        color:white;
        margin-bottom:20px;
    ">

    <h1>🧠 Insight AutoML</h1>

    <h3>AI-Powered Machine Learning & Data Analytics Platform</h3>

    <p style="font-size:18px;">
    📂 Upload &nbsp;&nbsp;|&nbsp;&nbsp;
    📊 Analyze &nbsp;&nbsp;|&nbsp;&nbsp;
    🤖 Train Models &nbsp;&nbsp;|&nbsp;&nbsp;
    🏆 Compare Results &nbsp;&nbsp;|&nbsp;&nbsp;
    💬 Ask AI
    </p>

    </div>
    """, unsafe_allow_html=True)

    st.info(
        "🚀 Upload your dataset, train multiple machine learning models, compare their performance, and interact with your data using the built-in AI Assistant powered by Ollama."
    )