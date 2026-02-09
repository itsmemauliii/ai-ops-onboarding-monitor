import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="AI Ops Monitor", layout="wide")

st.title("AI Ops Monitoring Dashboard")
st.subheader("SaaS Onboarding Bot Performance Overview")

# Load Data
@st.cache_data
def load_data():
    return pd.read_csv("data/mock_logs.csv", parse_dates=["timestamp"])

df = load_data()

# ---- KPI Calculations ----

total_sessions = len(df)
accuracy = (df["error_type"] == "none").mean() * 100
escalation_rate = df["escalation_flag"].mean() * 100
avg_response_time = df["response_time"].mean()

# ---- KPI Display ----

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Sessions", total_sessions)
col2.metric("Accuracy (%)", f"{accuracy:.2f}")
col3.metric("Escalation Rate (%)", f"{escalation_rate:.2f}")
col4.metric("Avg Response Time (s)", f"{avg_response_time:.2f}")

st.divider()

# ---- Retraining Alert ----

if accuracy < 85:
    st.error("⚠ Retraining Recommended: Accuracy below threshold (85%)")
else:
    st.success("✅ Model Performing Within Acceptable Threshold")

st.divider()

# ---- Error Breakdown Chart ----

st.subheader("Error Type Breakdown")

error_counts = df["error_type"].value_counts().reset_index()
error_counts.columns = ["error_type", "count"]

fig_errors = px.bar(
    error_counts,
    x="error_type",
    y="count",
    title="Distribution of Error Types"
)

st.plotly_chart(fig_errors, use_container_width=True)

# ---- Accuracy Over Time ----

st.subheader("Accuracy Trend Over Time")

df["is_correct"] = df["error_type"] == "none"
daily_accuracy = df.groupby("timestamp")["is_correct"].mean().reset_index()
daily_accuracy["is_correct"] *= 100

fig_trend = px.line(
    daily_accuracy,
    x="timestamp",
    y="is_correct",
    title="Daily Accuracy (%)"
)

st.plotly_chart(fig_trend, use_container_width=True)

# ---- Onboarding Step Performance ----

st.subheader("Onboarding Step Analysis")

step_accuracy = df.groupby("onboarding_step")["is_correct"].mean().reset_index()
step_accuracy["is_correct"] *= 100

fig_steps = px.bar(
    step_accuracy,
    x="onboarding_step",
    y="is_correct",
    title="Accuracy by Onboarding Step (%)"
)

st.plotly_chart(fig_steps, use_container_width=True)
