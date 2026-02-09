import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="AI Ops Monitor", layout="wide")

st.title("AI Ops Monitoring Platform")
st.subheader("Enterprise SaaS Onboarding Bot Intelligence")

# -----------------------------
# Sidebar Controls
# -----------------------------

st.sidebar.header("Configuration")

tier = st.sidebar.selectbox(
    "Select Pricing Tier",
    ["Starter", "Growth", "Enterprise"]
)

uploaded_file = st.sidebar.file_uploader("Upload AI Log CSV", type=["csv"])

# Tier-based thresholds
if tier == "Starter":
    accuracy_threshold = 80
    review_cost = 2
elif tier == "Growth":
    accuracy_threshold = 85
    review_cost = 1.5
else:
    accuracy_threshold = 90
    review_cost = 1

# -----------------------------
# Load Data
# -----------------------------

@st.cache_data
def load_data(file):
    return pd.read_csv(file, parse_dates=["timestamp"])

if uploaded_file:
    df = load_data(uploaded_file)
else:
    df = pd.read_csv("data/mock_logs.csv", parse_dates=["timestamp"])

# -----------------------------
# KPI Calculations
# -----------------------------

total_sessions = len(df)
accuracy = (df["error_type"] == "none").mean() * 100
escalation_rate = df["escalation_flag"].mean() * 100
avg_response_time = df["response_time"].mean()

df["is_correct"] = df["error_type"] == "none"

# Revenue risk estimation
error_count = len(df[df["error_type"] != "none"])
estimated_loss = error_count * review_cost

# -----------------------------
# KPI Display
# -----------------------------

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Sessions", total_sessions)
col2.metric("Accuracy (%)", f"{accuracy:.2f}")
col3.metric("Escalation Rate (%)", f"{escalation_rate:.2f}")
col4.metric("Avg Response Time (s)", f"{avg_response_time:.2f}")

st.divider()

# -----------------------------
# Retraining Alert
# -----------------------------

if accuracy < accuracy_threshold:
    st.error(f"⚠ Retraining Recommended (Threshold: {accuracy_threshold}%)")
else:
    st.success("✅ Model Within Acceptable Performance Range")

st.divider()

# -----------------------------
# Error Breakdown
# -----------------------------

st.subheader("Error Type Breakdown")

error_counts = df["error_type"].value_counts().reset_index()
error_counts.columns = ["error_type", "count"]

fig_errors = px.bar(error_counts, x="error_type", y="count")
st.plotly_chart(fig_errors, use_container_width=True)

# -----------------------------
# Accuracy Trend
# -----------------------------

st.subheader("Accuracy Trend Over Time")

daily_accuracy = df.groupby("timestamp")["is_correct"].mean().reset_index()
daily_accuracy["is_correct"] *= 100

fig_trend = px.line(daily_accuracy, x="timestamp", y="is_correct")
st.plotly_chart(fig_trend, use_container_width=True)

# -----------------------------
# Step Performance
# -----------------------------

st.subheader("Onboarding Step Performance")

step_accuracy = df.groupby("onboarding_step")["is_correct"].mean().reset_index()
step_accuracy["is_correct"] *= 100

fig_steps = px.bar(step_accuracy, x="onboarding_step", y="is_correct")
st.plotly_chart(fig_steps, use_container_width=True)

# -----------------------------
# Revenue Impact Panel
# -----------------------------

st.subheader("💰 Financial Impact Estimation")

st.metric("Estimated Monthly Quality Loss ($)", f"{estimated_loss:.2f}")
st.caption(f"Based on ${review_cost} review cost per error for {tier} tier.")
