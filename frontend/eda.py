import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



def show_eda(df):

    st.markdown("---")
    st.header("📊 Exploratory Data Analysis")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Rows", df.shape[0])

    with col2:
        st.metric("Columns", df.shape[1])

    st.subheader("Column Types")
    st.dataframe(df.dtypes.astype(str).reset_index().rename(
        columns={"index": "Column", 0: "Type"}
    ))

    st.subheader("Missing Values")
    st.dataframe(df.isnull().sum().reset_index().rename(
        columns={"index": "Column", 0: "Missing Values"}
    ))

    st.subheader("Statistics")
    st.dataframe(df.describe(include="all"))



    st.subheader("🔥 Correlation Heatmap")

    numeric_df = df.select_dtypes(include=["number"])

    if numeric_df.shape[1] > 1:

        corr = numeric_df.corr()

        fig, ax = plt.subplots(figsize=(10,6))

        sns.heatmap(
            corr,
            annot=True,
            cmap="coolwarm",
            ax=ax
        )

        st.pyplot(fig)

    else:

        st.info("No numerical columns available.")