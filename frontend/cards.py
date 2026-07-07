import streamlit as st


def show_cards(best_model, comparison_df):

    best_accuracy = comparison_df["Accuracy"].max()

    total_models = len(comparison_df)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            label="🏆 Best Model",
            value=best_model
        )

    with col2:
        st.metric(
            label="🎯 Best Accuracy",
            value=f"{best_accuracy:.2%}"
        )

    with col3:
        st.metric(
            label="🤖 Models Trained",
            value=total_models
        )