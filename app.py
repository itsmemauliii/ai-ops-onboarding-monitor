import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="AI Ops Monitor",
    page_icon="🤖",
    layout="wide"
)

# -----------------------------
# Custom Minimal Styling
# -----------------------------

st.markdown("""
<style>
.main {
    background-color: #0E1117;
}
.block-container {
    padding-top: 2rem;
}
h1, h2, h3 {
    color: #FFFFFF;
}
.metric-card {
    background-color: #1C1F26;
    padding: 20px;
    border-radius: 12px;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# Header
# -----------------------------

st.title("🤖 AI Onboarding Intelligence Platform")
st.caption("Operational Visibility for AI-Powered SaaS Products")

st.divider()

# -----------------------------
# Sidebar
# -----------------------------

st.sidebar.header("Plan Configuration")

tier = st.sidebar.radio(
    "Select Pricing Tier",
    ["Starter", "Growth", "Enterprise"]
)

uploaded_file = st.sidebar.file_uploader("Upload AI Log CSV", type=["csv"])

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

df["is_correct"] = df["error_type"] == "none"

# -----------------------------
# KPI Calculations
# -----------------------------

total_sessions = len(df)
accuracy = df["is_correct"].mean() * 100
escalation_rate = df["escalation_flag"].mean() * 100
avg_response_time = df["response_time"].mean()
error_count = len(df[df["error_type"] != "none"])
estimated_loss = error_count * review_cost

# -----------------------------
# KPI Display (Cleaner Layout)
# -----------------------------

st.subheader("📊 Core Performance Metrics")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Sessions", f"{total_sessions:,}")
col2.metric("Accuracy", f"{accuracy:.2f}%")
col3.metric("Escalation Rate", f"{escalation_rate:.2f}%")
col4.metric("Avg Response Time", f"{avg_response_time:.2f}s")

st.divider()

# -----------------------------
# Model Health Status
# -----------------------------

st.subheader("🧠 Model Health Status")

if accuracy < accuracy_threshold:
    st.error(f"Performance Below Threshold ({accuracy_threshold}%) — Retraining Recommended")
else:
    st.success("Model Performing Within Acceptable Range")

st.divider()

# -----------------------------
# Tier-Based Analytics
# -----------------------------

st.subheader("📈 Performance Insights")

error_counts = df["error_type"].value_counts().reset_index()
error_counts.columns = ["error_type", "count"]

fig_errors = px.bar(
    error_counts,
    x="error_type",
    y="count",
    title="Error Breakdown"
)

st.plotly_chart(fig_errors, use_container_width=True)

if tier in ["Growth", "Enterprise"]:
    daily_accuracy = df.groupby("timestamp")["is_correct"].mean().reset_index()
    daily_accuracy["is_correct"] *= 100

    fig_trend = px.line(
        daily_accuracy,
        x="timestamp",
        y="is_correct",
        title="Accuracy Trend Over Time"
    )

    st.plotly_chart(fig_trend, use_container_width=True)

if tier == "Enterprise":
    step_accuracy = df.groupby("onboarding_step")["is_correct"].mean().reset_index()
    step_accuracy["is_correct"] *= 100

    fig_steps = px.bar(
        step_accuracy,
        x="onboarding_step",
        y="is_correct",
        title="Onboarding Step Performance"
    )

    st.plotly_chart(fig_steps, use_container_width=True)

    # Churn Risk
    churn_risk = 0

    if accuracy < 85:
        churn_risk += 30
    if escalation_rate > 15:
        churn_risk += 30
    if avg_response_time > 2.5:
        churn_risk += 20

    step2_accuracy = (
        df[df["onboarding_step"] == 2]["is_correct"].mean() * 100
    )

    if step2_accuracy < 80:
        churn_risk += 20

    churn_risk = min(churn_risk, 100)

    st.subheader("⚠ Churn Risk Indicator")

    if churn_risk < 30:
        st.success(f"Low Risk — {churn_risk}%")
    elif churn_risk < 60:
        st.warning(f"Moderate Risk — {churn_risk}%")
    else:
        st.error(f"High Risk — {churn_risk}%")

st.divider()

# -----------------------------
# Financial Impact Section
# -----------------------------

st.subheader("💰 Financial Impact")

st.metric("Estimated Monthly Quality Loss", f"${estimated_loss:,.2f}")
st.caption(f"Calculated using ${review_cost} review cost per error under {tier} plan.")

# -----------------------------
# Upgrade CTA
# -----------------------------

if tier in ["Starter", "Growth"]:
    st.markdown("---")
    st.info("Upgrade to Enterprise for Predictive Churn & Advanced Insights")
    st.button("Upgrade Plan")

# -----------------------------
# Executive Summary
# -----------------------------

st.divider()
st.subheader("📋 Executive Summary")

st.markdown(f"""
- Total Sessions Processed: **{total_sessions:,}**
- Current Accuracy: **{accuracy:.2f}%**
- Escalation Rate: **{escalation_rate:.2f}%**
- Estimated Monthly Quality Loss: **${estimated_loss:,.2f}**
- Active Plan: **{tier}**
""")
