import streamlit as st
import requests
import pandas as pd
import os

from cards import show_cards
from styles import load_css
from header import show_header
from sidebar import show_sidebar
from charts import show_accuracy_chart
from components import show_leaderboard
from eda import show_eda

BACKEND_URL = os.getenv(
    "BACKEND_URL",
    "https://insightai-automl.onrender.com"
)

st.set_page_config(
    page_title="Insight AutoML | Data Analyst",
    page_icon="🤖",
    layout="wide"
)

st.markdown(load_css(), unsafe_allow_html=True)

show_sidebar()
show_header()

st.markdown("""
### 🚀 Machine Learning & Data Analytics Platform

[Upload your dataset and let Insight AutoML]:

✅ Clean Data

✅ Train Multiple ML Models

✅ Compare Performance

---
""")

uploaded_file = st.file_uploader(
    "📂 Upload CSV Dataset",
    type=["csv"]
)

if uploaded_file is not None:

    os.makedirs("datasets/raw", exist_ok=True)

    save_path = f"datasets/raw/{uploaded_file.name}"

    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    df = pd.read_csv(save_path)

    st.subheader("📄 Dataset Preview")

    st.dataframe(
        df.head(),
        use_container_width=True
    )
    show_eda(df)


    c1, c2 = st.columns(2)

    with c1:
        st.metric("Rows", df.shape[0])

    with c2:
        st.metric("Columns", df.shape[1])

    target_column = st.selectbox(
        "🎯 Select Target Column",
        df.columns
    )
if st.button("🚀 Train Models", use_container_width=True):

    with st.spinner("Training models... Please wait..."):

        try:

            response = requests.post(
                f"{BACKEND_URL}/train",
                    files={
                        "file": (
                            uploaded_file.name,
                            uploaded_file.getvalue(),
                            "text/csv",
                        )
                    },
                    data={
                        "target_column": target_column,
                    },
                    timeout=300
         )
            st.write("Status Code:", response.status_code)
            st.write("Content-Type:", response.headers.get("Content-Type"))
            st.write("Response Preview:")
            st.code(response.text[:500])

            if response.status_code != 200:
                st.error("❌ Training Failed")
                st.text(response.text)
                st.stop()

            st.session_state["result"] = response.json()
            st.session_state["df"] = df

        except Exception as e:
            st.error(f"❌ {e}")
            st.stop()


# ===========================
# SHOW RESULTS ONLY IF TRAINED
# ===========================

if "result" in st.session_state:

    st.success("✅ Training Completed Successfully!")

    result = st.session_state["result"]
    metrics = result["metrics"]

    comparison = []

    for model, values in metrics.items():

        comparison.append({
            "Model": model,
            "Accuracy": values["accuracy"],
            "Precision": values["precision"],
            "Recall": values["recall"],
            "F1 Score": values["f1_score"]
        })

    comparison_df = pd.DataFrame(comparison)

    comparison_df = comparison_df.sort_values(
        by="Accuracy",
        ascending=False
    )

    st.session_state["comparison_df"] = comparison_df

    st.markdown("---")

    show_cards(
        result["best_model"],
        comparison_df
    )

    st.markdown("---")

    show_leaderboard(comparison_df)

    st.markdown("---")

    show_accuracy_chart(comparison_df)

    st.markdown("---")

    st.subheader("🤖 AI Dataset Assistant")

st.info("""
🚀 **Coming Soon in Version 1.1**

The AI Dataset Assistant is currently under development.

### Planned Features
- 🤖 Google Gemini Integration
- 📊 Natural Language Dataset Analysis
- 💡 Smart Feature Engineering Suggestions
- 📈 Model Improvement Recommendations
- 📝 Automatic Dataset Insights

Thank you for trying **Insight AutoML**! Stay tuned for the next release.
""")