import streamlit as st


def show_sidebar():

    st.sidebar.markdown("# 🧠 Insight AutoML")

    st.sidebar.caption("Automated Machine Learning & Data Analytics Platform")

    st.sidebar.markdown("---")

    st.sidebar.success("🟢 Backend Connected")

   
    st.sidebar.markdown("""
    ## 🚀 Workflow

    ✅ Upload Dataset

    ✅ Exploratory Data Analysis

    ✅ Select Target Column

    ✅ Train ML Models

    ✅ Compare Performance
    """)

    st.sidebar.markdown("---")

    st.sidebar.info("""
    ### 💡 Quick Tips

    ✅ Upload a clean CSV dataset

    🎯 Choose the correct target column

    📊 Compare multiple ML models

    🏆 Use the highest accuracy model

    📈 Review performance metrics
    """)

    st.sidebar.markdown("---")

    st.sidebar.markdown("## 🛠 Tech Stack")

    st.sidebar.markdown("""
    - 🐍 **Python**
    - ⚡ **FastAPI**
    - 🎨 **Streamlit**
    - 🤖 **Scikit-learn**
    - 📊 **Pandas**
    - 📈 **NumPy**
    """)

    st.sidebar.markdown("---")

 
    st.sidebar.info(
            """
        💡 **Tips**

        • Upload a clean CSV dataset

        • Select the correct target column

        • Compare model performance

        • Download the results.
        """
        )

    st.sidebar.markdown("-----")

    st.sidebar.caption("Version • v1.0.0")

    st.sidebar.caption("Made with 💜 by Nikhil Tripathi")