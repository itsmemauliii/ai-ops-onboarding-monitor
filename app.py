import streamlit as st

st.set_page_config(layout="wide")

# -----------------------------
# Session State Setup
# -----------------------------

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "page" not in st.session_state:
    st.session_state.page = "Dashboard"

# -----------------------------
# Landing Page (Before Login)
# -----------------------------

if not st.session_state.logged_in:

    st.markdown("""
    <style>
    .hero {
        text-align:center;
        padding:80px 20px;
        background: linear-gradient(90deg,#0f2027,#203a43,#2c5364);
        border-radius:20px;
        color:white;
    }
    .pricing-card {
        background:white;
        padding:30px;
        border-radius:15px;
        box-shadow:0 8px 20px rgba(0,0,0,0.1);
        text-align:center;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="hero">
        <h1>🚀 AI Ops Intelligence Platform</h1>
        <p>Operational visibility for AI-powered SaaS products</p>
    </div>
    """, unsafe_allow_html=True)

    st.write("")
    st.write("")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown('<div class="pricing-card"><h3>Starter</h3><h2>$29</h2><p>Basic monitoring</p></div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="pricing-card"><h3>Growth</h3><h2>$99</h2><p>Analytics & insights</p></div>', unsafe_allow_html=True)

    with col3:
        st.markdown('<div class="pricing-card"><h3>Enterprise</h3><h2>$249</h2><p>Full AI intelligence suite</p></div>', unsafe_allow_html=True)

    st.write("")
    st.write("")

    if st.button("Login to Platform"):
        st.session_state.logged_in = True
        st.rerun()

    st.stop()

# -----------------------------
# Custom Navbar
# -----------------------------

nav_col1, nav_col2, nav_col3, nav_col4 = st.columns([2,1,1,1])

with nav_col1:
    st.markdown("### 🤖 AI Ops Monitor")

with nav_col2:
    if st.button("Dashboard"):
        st.session_state.page = "Dashboard"

with nav_col3:
    if st.button("Billing"):
        st.session_state.page = "Billing"

with nav_col4:
    if st.button("Settings"):
        st.session_state.page = "Settings"

st.divider()

# -----------------------------
# Page Router
# -----------------------------

if st.session_state.page == "Dashboard":
    import pages.dashboard as dashboard
    dashboard.render()

elif st.session_state.page == "Billing":
    import pages.billing as billing
    billing.render()

elif st.session_state.page == "Settings":
    import pages.settings as settings
    settings.render()
