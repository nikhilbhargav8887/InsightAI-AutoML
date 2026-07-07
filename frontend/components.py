import streamlit as st


def show_leaderboard(comparison_df):

    st.subheader("🏆 Model Leaderboard")

    comparison_df = comparison_df.sort_values(
        by="Accuracy",
        ascending=False
    )

    medals = ["🥇", "🥈", "🥉"]

    for i, row in comparison_df.iterrows():

        icon = medals[i] if i < 3 else "🏅"

        st.markdown(
            f"""
**{icon} {row['Model']}**

Accuracy : **{row['Accuracy']:.2%}**

---
"""
        )