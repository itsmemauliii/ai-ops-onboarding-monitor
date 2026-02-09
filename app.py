import streamlit as st

st.set_page_config(layout="wide")

# -----------------------------
# Session State Setup
# -----------------------------

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "page" not in st.session_state:
    st.session_state.page = "Dashboard"

if "theme" not in st.session_state:
    st.session_state.theme = "Dark"

# -----------------------------
# THEME STYLES
# -----------------------------

def apply_theme():

    if st.session_state.theme == "Dark":
        st.markdown("""
        <style>
        body { background-color:#0e1117; color:white; }
        .stApp { background-color:#0e1117; color:white; }
        </style>
        """, unsafe_allow_html=True)

    elif st.session_state.theme == "Light":
        st.markdown("""
        <style>
        body { background-color:white; color:black; }
        .stApp { background-color:white; color:black; }
        </style>
        """, unsafe_allow_html=True)

    elif st.session_state.theme == "Rainbow":
        st.markdown("""
        <style>
        .stApp {
            background: linear-gradient(135deg,
            #ff0000,
            #ff7f00,
            #ffff00,
            #00ff00,
            #0000ff,
            #4b0082,
            #9400d3);
            background-size: 400% 400%;
            animation: gradientMove 10s ease infinite;
            color: white !important;
        }

        @keyframes gradientMove {
            0% { background-position:0% 50% }
            50% { background-position:100% 50% }
            100% { background-position:0% 50% }
        }

        h1, h2, h3, h4, h5, h6, p, span, div {
            color: white !important;
            font-weight: 500;
        }

        .stMetric {
            background: rgba(0,0,0,0.6);
            padding:15px;
            border-radius:12px;
        }

        button {
            background-color:black !important;
            color:white !important;
            border-radius:10px !important;
        }

        </style>
        """, unsafe_allow_html=True)

apply_theme()

# -----------------------------
# Landing Page
# -----------------------------

if not st.session_state.logged_in:

    st.title("🚀 AI Ops Intelligence Platform")
    st.write("Operational visibility for AI-powered SaaS products")

    if st.button("Login to Platform"):
        st.session_state.logged_in = True
        st.rerun()

    st.stop()

# -----------------------------
# Custom Navbar
# -----------------------------

nav1, nav2, nav3, nav4 = st.columns([2,1,1,1])

with nav1:
    st.markdown("### 🤖 AI Ops Monitor")

with nav2:
    if st.button("Dashboard"):
        st.session_state.page = "Dashboard"

with nav3:
    if st.button("Billing"):
        st.session_state.page = "Billing"

with nav4:
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
