import streamlit as st
import requests
import pandas as pd
import os

st.set_page_config(
    page_title="AI Powered Data Analyst",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Powered Data Analyst")
st.markdown("### Upload a dataset and let AI train multiple Machine Learning models automatically.")

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
    st.dataframe(df.head(), use_container_width=True)

    st.write(f"Rows: **{df.shape[0]}**")
    st.write(f"Columns: **{df.shape[1]}**")

    target_column = st.selectbox(
        "🎯 Select Target Column",
        df.columns
    )

    if st.button("🚀 Train AI"):

        with st.spinner("Training models... Please wait..."):

            response = requests.post(
                "http://127.0.0.1:8000/train",
                json={
                    "file_path": save_path,
                    "target_column": target_column
                }
            )

        if response.status_code == 200:

            result = response.json()

            st.success("✅ Training Completed Successfully!")

            st.markdown("---")

            st.subheader("🏆 Best Model")

            st.success(result["best_model"])

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

            st.markdown("---")

            st.subheader("📊 Model Comparison")

            st.dataframe(
                comparison_df,
                use_container_width=True
            )

            st.markdown("---")

            st.subheader("📈 Accuracy Comparison")

            chart_df = comparison_df.set_index("Model")

            st.bar_chart(chart_df["Accuracy"])

            st.markdown("---")

            st.subheader("📌 Performance Summary")

            col1, col2 = st.columns(2)

            with col1:
                st.metric(
                    "Best Accuracy",
                    f"{comparison_df['Accuracy'].max():.4f}"
                )

            with col2:
                st.metric(
                    "Total Models",
                    len(comparison_df)
                )

        else:

            st.error("❌ Training Failed")

            try:
                st.json(response.json())
            except Exception:
                st.text(response.text)