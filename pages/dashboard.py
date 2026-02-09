import streamlit as st

def render():

    st.title("📊 Dashboard")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Sessions", "2,450")
    col2.metric("Accuracy", "94%")
    col3.metric("Escalation Rate", "6%")
    col4.metric("Avg Response Time", "1.2s")

    st.divider()
    st.success("System Operational")
