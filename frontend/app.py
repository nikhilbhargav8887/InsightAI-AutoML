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

BACKEND_URL = os.getenv("BACKEND_URL", "http://127.0.0.1:8000")


st.set_page_config(
    page_title="Insight AutoML | AI Data Analyst",
    page_icon="🤖",
    layout="wide"
)

st.markdown(load_css(), unsafe_allow_html=True)

show_sidebar()
show_header()

st.markdown("""
### 🚀 Intelligent Machine Learning & Data Analytics Platform

[Upload your dataset and let Insight AutoML]:

✅ Clean Data

✅ Train Multiple ML Models

✅ Compare Performance

✅ Generate AI Insights

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

    if st.button("🚀 Train AI", use_container_width=True):

     with st.spinner("Training models... Please wait..."):

        try:

            response = requests.post(
                f"{BACKEND_URL}/train",
                files={
                    "file": (
                        uploaded_file.name,
                        uploaded_file.getvalue(),
                        "text/csv"
                    )
                },
                data={
                    "target_column": target_column
                }
            )

            if response.status_code != 200:
                st.error("❌ Training Failed")
                st.text(response.text)
                st.stop()

            result = response.json()

            st.session_state["result"] = result
            st.session_state["df"] = df

        except Exception as e:
            st.error(f"❌ {e}")
            st.stop()

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

    st.markdown("""
    Ask questions about your uploaded dataset, model performance, preprocessing,
    feature engineering, or machine learning concepts.
    """)

    with st.expander("💡 Example Questions"):

        st.markdown("""
    - Which model performed the best?
    - Why is Random Forest better than Logistic Regression?
    - Is my dataset balanced?
    - Which columns contain missing values?
    - Suggest preprocessing steps.
    - Suggest feature engineering.
    - How can I improve accuracy?
    """)

    question = st.text_input(
        "💬 Ask your question",
        placeholder="Example: Which model performed best and why?"
    )

    if st.button("🚀 Ask AI", use_container_width=True):

        if "result" not in st.session_state:
            st.warning("⚠️ Please train the model first.")
            st.stop()

        if "df" not in st.session_state:
            st.warning("⚠️ Please upload a dataset first.")
            st.stop()

        with st.spinner("🤖 Insight AutoML is analyzing your dataset..."):

            df = st.session_state["df"]

            dataset_info = {
                "columns": df.columns.tolist(),
                "shape": list(df.shape),
                "missing_values": df.isnull().sum().to_dict(),
                "dtypes": df.dtypes.astype(str).to_dict(),
                "statistics": df.describe(include="all").fillna("").to_dict()
            }

            response = requests.post(
                f"{BACKEND_URL}/chat",
                json={
                    "dataset_info": dataset_info,
                    "metrics": st.session_state["result"]["metrics"],
                    "question": question
                }
            )

            if response.status_code == 200:

                answer = response.json()["answer"]

                st.markdown("## 🤖 AI Response")

                st.markdown(
                    f"""
    <div style="
    background:#F4F6F8;
    padding:20px;
    border-radius:12px;
    border-left:6px solid #2563EB;
    ">

    {answer}

    </div>
    """,
                    unsafe_allow_html=True,
                )

            else:
                st.error(response.text)