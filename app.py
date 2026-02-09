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
    "Active Plan",
    ["Starter", "Growth", "Enterprise"]
)

uploaded_file = st.sidebar.file_uploader("Upload AI Log CSV", type=["csv"])

# -----------------------------
# Theme System
# -----------------------------

if ui_mode == "Dark Mode":
    bg_color = "#0E1117"
    card_color = "#1C1F26"
    text_color = "white"
    header_gradient = None

elif ui_mode == "Light Mode":
    bg_color = "#F4F6FA"
    card_color = "#FFFFFF"
    text_color = "#111111"
    header_gradient = None

elif ui_mode == "Rainbow Mode":
    bg_color = "#0E1117"
    card_color = "rgba(255,255,255,0.08)"
    text_color = "white"
    header_gradient = "linear-gradient(90deg, #ff6a00, #ee0979, #00c6ff)"

# -----------------------------
# Force Text Visibility (Fix)
# -----------------------------

st.markdown(f"""
<style>
.stApp {{
    background-color: {bg_color};
    color: {text_color};
}}

* {{
    color: {text_color} !important;
}}

section[data-testid="stSidebar"] {{
    background-color: {card_color};
}}

.block-container {{
    padding-top: 2rem;
}}

div[data-testid="metric-container"] {{
    background-color: {card_color};
    padding: 15px;
    border-radius: 15px;
}}

div[data-testid="stAlert"] {{
    color: white !important;
}}

h1, h2, h3, h4, p, label, span {{
    color: {text_color} !important;
}}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# Header
# -----------------------------

if ui_mode == "Rainbow Mode":
    st.markdown(f"""
    <div style='
        padding: 30px;
        border-radius: 20px;
        background: {header_gradient};
        text-align: center;
        font-size: 2.5rem;
        font-weight: bold;
        color: white;
        margin-bottom: 20px;
    '>
        🌈 AI Intelligence Command Center
    </div>
    """, unsafe_allow_html=True)
else:
    st.title("🤖 AI Onboarding Intelligence Platform")

st.caption("Operational Visibility for AI-Powered SaaS Products")

st.divider()

# -----------------------------
# Pricing Config
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
# Model Health
# -----------------------------

st.subheader("🧠 Model Health")

if accuracy < accuracy_threshold:
    st.error(f"Performance Below Threshold ({accuracy_threshold}%) — Retraining Recommended")
else:
    st.success("Model Performing Within Acceptable Range")

st.divider()

# -----------------------------
# Insights
# -----------------------------

st.subheader("📈 Insights")

error_counts = df["error_type"].value_counts().reset_index()
error_counts.columns = ["error_type", "count"]

fig_errors = px.bar(error_counts, x="error_type", y="count")
st.plotly_chart(fig_errors, use_container_width=True)

st.divider()

# -----------------------------
# Financial Impact
# -----------------------------

st.subheader("💰 Financial Impact")
st.metric("Estimated Monthly Quality Loss", f"${estimated_loss:,.2f}")

st.divider()

# -----------------------------
# Pricing Section (NEW)
# -----------------------------

st.subheader("💳 Upgrade Plans")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### Starter")
    st.markdown("**$29 / month**")
    st.markdown("- Basic Monitoring")
    st.markdown("- Error Breakdown")
    st.markdown("- Email Support")
    if st.button("Choose Starter"):
        st.success("Starter Plan Activated")

with col2:
    st.markdown("### Growth")
    st.markdown("**$99 / month**")
    st.markdown("- Trend Analytics")
    st.markdown("- Escalation Insights")
    st.markdown("- Priority Support")
    if st.button("Upgrade to Growth"):
        st.success("Redirecting to Payment Gateway...")

with col3:
    st.markdown("### Enterprise")
    st.markdown("**$249 / month**")
    st.markdown("- Churn Prediction")
    st.markdown("- Advanced AI Insights")
    st.markdown("- Dedicated Manager")
    if st.button("Upgrade to Enterprise"):
        st.success("Redirecting to Enterprise Sales Team...")

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
- Active Plan: **{tier}**
""")
