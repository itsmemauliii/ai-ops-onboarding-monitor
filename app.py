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

    st.markdown("""
    <style>
    .login-container {
        display:flex;
        justify-content:center;
        align-items:center;
        height:80vh;
    }

    .login-card {
        background: rgba(255,255,255,0.05);
        backdrop-filter: blur(15px);
        padding: 60px;
        border-radius: 20px;
        text-align:center;
        box-shadow: 0 0 40px rgba(0,0,0,0.4);
        animation: floatCard 4s ease-in-out infinite;
    }

    @keyframes floatCard {
        0% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
        100% { transform: translateY(0px); }
    }

    .login-title {
        font-size: 42px;
        font-weight: 700;
        color: white;
        margin-bottom: 10px;
    }

    .login-subtitle {
        font-size: 18px;
        color: #cccccc;
        margin-bottom: 40px;
    }

    .login-btn button {
        background: linear-gradient(90deg, #ff6a00, #ee0979);
        color: white !important;
        font-weight: 600;
        border-radius: 30px;
        padding: 12px 40px;
        font-size: 16px;
        border: none;
        transition: 0.3s ease;
    }

    .login-btn button:hover {
        transform: scale(1.05);
        box-shadow: 0 0 20px rgba(255,105,180,0.6);
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="login-container">', unsafe_allow_html=True)
    st.markdown('<div class="login-card">', unsafe_allow_html=True)

    st.markdown('<div class="login-title">🚀 AI Ops Intelligence Platform</div>', unsafe_allow_html=True)
    st.markdown('<div class="login-subtitle">Operational visibility for AI-powered SaaS products</div>', unsafe_allow_html=True)

    st.markdown('<div class="login-btn">', unsafe_allow_html=True)
    if st.button("Enter Platform"):
        st.session_state.logged_in = True
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('</div></div>', unsafe_allow_html=True)

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
