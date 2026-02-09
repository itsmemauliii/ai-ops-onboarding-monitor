import streamlit as st
import pandas as pd
import plotly.express as px

def render():

    st.title("AI Performance Dashboard")

    df = pd.read_csv("data/mock_logs.csv")

    total = len(df)
    accuracy = (df["error_type"] == "none").mean() * 100
    escalation = df["escalation_flag"].mean() * 100

    col1, col2, col3 = st.columns(3)
    col1.metric("Sessions", total)
    col2.metric("Accuracy", f"{accuracy:.2f}%")
    col3.metric("Escalation Rate", f"{escalation:.2f}%")

    st.divider()

    fig = px.histogram(df, x="error_type")
    st.plotly_chart(fig, use_container_width=True)
