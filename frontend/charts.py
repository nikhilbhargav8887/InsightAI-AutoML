import streamlit as st
import plotly.express as px


def show_accuracy_chart(comparison_df):

    fig = px.bar(
        comparison_df,
        x="Model",
        y="Accuracy",
        color="Accuracy",
        text="Accuracy",
        title="📊 Model Accuracy Comparison"
    )

    fig.update_traces(
        texttemplate="%{text:.2f}",
        textposition="outside"
    )

    fig.update_layout(
        template="plotly_dark",
        height=500,
        xaxis_title="Model",
        yaxis_title="Accuracy",
        title_x=0.5
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )