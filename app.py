import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="AI Ops Monitor",
    page_icon="🚀",
    layout="wide"
)

# -----------------------------
# Sidebar
# -----------------------------

st.sidebar.title("⚙️ Settings")

ui_mode = st.sidebar.selectbox(
    "Choose UI Mode",
    ["Dark Mode", "Light Mode", "Rainbow Mode"]
)

tier = st.sidebar.radio(
    "Select Pricing Tier",
    ["Starter", "Growth", "Enterprise"]
)

uploaded_file = st.sidebar.file_uploader("Upload AI Log CSV", type=["csv"])

# -----------------------------
# Dynamic Themes
# -----------------------------

if ui_mode == "Dark Mode":
    bg_color = "#0E1117"
    card_color = "#1C1F26"
    text_color = "white"

elif ui_mode == "Light Mode":
    bg_color = "#F5F7FA"
    card_color = "#FFFFFF"
    text_color = "#111111"

elif ui_mode == "Rainbow Mode":
    bg_color = "linear-gradient(135deg, #1e3c72, #2a5298, #ff6a00, #ee0979)"
    card_color = "rgba(255,255,255,0.1)"
    text_color = "white"

# Apply CSS
st.markdown(f"""
<style>
.stApp {{
    background: {bg_color};
    color: {text_color};
}}

section[data-testid="stSidebar"] {{
    background-color: {card_color};
}}

.block-container {{
    padding-top: 2rem;
}}

.metric-card {{
    background-color: {card_color};
    padding: 20px;
    border-radius: 15px;
}}

h1, h2, h3, h4 {{
    color: {text_color};
}}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# Header
# -----------------------------

if ui_mode == "Rainbow Mode":
    st.markdown("""
    <h1 style='text-align: center; font-size: 3rem; 
    background: linear-gradient(90deg, #ff6a00, #ee0979, #00c6ff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;'>
    🌈 AI Intelligence Command Center
    </h1>
    """, unsafe_allow_html=True)
else:
    st.title("🤖 AI Onboarding Intelligence Platform")

st.caption("Operational Visibility for AI-Powered SaaS Products")

st.divider()

# -----------------------------
# Pricing Tier Logic
# -----------------------------

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
# KPIs
# -----------------------------

total_sessions = len(df)
accuracy = df["is_correct"].mean() * 100
escalation_rate = df["escalation_flag"].mean() * 100
avg_response_time = df["response_time"].mean()
error_count = len(df[df["error_type"] != "none"])
estimated_loss = error_count * review_cost

st.subheader("📊 Performance Overview")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Sessions", f"{total_sessions:,}")
col2.metric("Accuracy", f"{accuracy:.2f}%")
col3.metric("Escalation Rate", f"{escalation_rate:.2f}%")
col4.metric("Avg Response Time", f"{avg_response_time:.2f}s")

st.divider()

# -----------------------------
# Health Status
# -----------------------------

st.subheader("🧠 Model Health")

if accuracy < accuracy_threshold:
    st.error("Performance Below Threshold — Retraining Recommended")
else:
    st.success("Model Performing Within Acceptable Range")

st.divider()

# -----------------------------
# Analytics
# -----------------------------

st.subheader("📈 Insights")

error_counts = df["error_type"].value_counts().reset_index()
error_counts.columns = ["error_type", "count"]
fig_errors = px.bar(error_counts, x="error_type", y="count")
st.plotly_chart(fig_errors, use_container_width=True)

if tier in ["Growth", "Enterprise"]:
    daily_accuracy = df.groupby("timestamp")["is_correct"].mean().reset_index()
    daily_accuracy["is_correct"] *= 100
    fig_trend = px.line(daily_accuracy, x="timestamp", y="is_correct")
    st.plotly_chart(fig_trend, use_container_width=True)

if tier == "Enterprise":
    step_accuracy = df.groupby("onboarding_step")["is_correct"].mean().reset_index()
    step_accuracy["is_correct"] *= 100
    fig_steps = px.bar(step_accuracy, x="onboarding_step", y="is_correct")
    st.plotly_chart(fig_steps, use_container_width=True)

st.divider()

# -----------------------------
# Financial Impact
# -----------------------------

st.subheader("💰 Financial Impact")
st.metric("Estimated Monthly Quality Loss", f"${estimated_loss:,.2f}")

st.divider()

# -----------------------------
# Executive Summary
# -----------------------------

st.subheader("📋 Executive Summary")

st.markdown(f"""
- Sessions Processed: **{total_sessions:,}**
- Accuracy: **{accuracy:.2f}%**
- Escalation Rate: **{escalation_rate:.2f}%**
- Estimated Monthly Loss: **${estimated_loss:,.2f}**
- Plan: **{tier}**
""")
