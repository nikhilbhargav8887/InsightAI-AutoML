import streamlit as st


def show_sidebar():

    st.sidebar.markdown("# 🧠 Insight AutoML")

    st.sidebar.caption("AI-Powered Data Analytics Platform")

    st.sidebar.markdown("---")

    st.sidebar.success("🟢 Backend Connected")

    st.sidebar.markdown("## 🚀 Workflow")

    st.sidebar.markdown("""
✅ **1. Upload CSV Dataset**

✅ **2. Explore Dataset (EDA)**

✅ **3. Select Target Column**

✅ **4. Train Multiple ML Models**

✅ **5. Compare Model Performance**

✅ **6. Ask AI About Your Dataset**
""")

    st.sidebar.markdown("---")

    st.sidebar.markdown("## 🛠 Tech Stack")

    st.sidebar.markdown("""
- 🐍 Python
- ⚡ FastAPI
- 🎨 Streamlit
- 🤖 Ollama (Llama 3)
- 📊 Scikit-learn
- 🐼 Pandas
""")

    st.sidebar.markdown("---")

    st.sidebar.info(
        "💡 Tip: Ask the AI questions like:\n\n"
        "- Which model performed best?\n"
        "- Is my dataset balanced?\n"
        "- Suggest preprocessing steps."
    )

    st.sidebar.markdown("---")

    st.sidebar.caption("Version 1.0")

    st.sidebar.caption("Made with ❤️ by Nikhil Tripathi")