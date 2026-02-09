import streamlit as st
import time

st.set_page_config(layout="wide")

# -----------------------------
# SESSION STATE INIT
# -----------------------------

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "page" not in st.session_state:
    st.session_state.page = "Dashboard"

if "theme" not in st.session_state:
    st.session_state.theme = "Dark"

if "login_failed" not in st.session_state:
    st.session_state.login_failed = False

# -----------------------------
# THEME ENGINE
# -----------------------------

def apply_theme():

    if st.session_state.theme == "Dark":
        bg = "#0E1117"
        text = "white"

    elif st.session_state.theme == "Light":
        bg = "#F5F7FA"
        text = "#111111"

    elif st.session_state.theme == "Rainbow":
        st.markdown("""
        <style>
        .stApp {
            background: linear-gradient(135deg,
            #ff0000,#ff7f00,#ffff00,
            #00ff00,#0000ff,#4b0082,#9400d3);
            background-size: 400% 400%;
            animation: gradientMove 10s ease infinite;
            color: white !important;
        }
        @keyframes gradientMove {
            0% { background-position:0% 50% }
            50% { background-position:100% 50% }
            100% { background-position:0% 50% }
        }
        h1,h2,h3,h4,h5,h6,p,span,div {
            color:white !important;
        }
        </style>
        """, unsafe_allow_html=True)
        return

    st.markdown(f"""
    <style>
    .stApp {{
        background-color: {bg};
        color: {text};
    }}
    </style>
    """, unsafe_allow_html=True)

apply_theme()

# -----------------------------
# LOGIN PAGE
# -----------------------------

if not st.session_state.logged_in:

    st.markdown("""
    <style>
    .login-wrapper {
        display:flex;
        justify-content:center;
        align-items:center;
        height:100vh;
    }
    .login-card {
        background: rgba(255,255,255,0.05);
        backdrop-filter: blur(20px);
        padding:60px;
        border-radius:20px;
        width:420px;
        text-align:center;
        box-shadow:0 0 60px rgba(0,0,0,0.6);
        animation: fadeIn 1s ease;
    }
    @keyframes fadeIn {
        from {opacity:0; transform: translateY(20px);}
        to {opacity:1; transform: translateY(0);}
    }
    .typing {
        overflow: hidden;
        white-space: nowrap;
        border-right: 3px solid orange;
        width: 0;
        animation: typing 3s steps(40,end) forwards, blink .8s infinite;
        margin:15px auto 30px auto;
        color:#bbbbbb;
    }
    @keyframes typing {
        from { width: 0 }
        to { width: 100% }
    }
    @keyframes blink {
        50% { border-color: transparent }
    }
    .shake { animation: shake 0.4s; }
    @keyframes shake {
        25% { transform: translateX(-5px); }
        50% { transform: translateX(5px); }
        75% { transform: translateX(-5px); }
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="login-wrapper">', unsafe_allow_html=True)

    card_class = "login-card"
    if st.session_state.login_failed:
        card_class += " shake"

    st.markdown(f'<div class="{card_class}">', unsafe_allow_html=True)

    st.markdown("## 🚀 AI Ops Platform")
    st.markdown('<div class="typing">Secure Access to Your AI Infrastructure</div>', unsafe_allow_html=True)

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    remember = st.checkbox("Remember Me")

    login_btn = st.button("Login", type="primary")

    if login_btn:
        if email == "admin@aiops.com" and password == "1234":
            st.session_state.login_failed = False

            loader = st.empty()
            for i in range(101):
                loader.markdown(f"### 🍬 Cooking Sweet Intelligence... {i}%")
                time.sleep(0.02)
            loader.empty()

            st.session_state.logged_in = True
            st.rerun()
        else:
            st.session_state.login_failed = True
            st.error("Invalid credentials. Use admin@aiops.com / 1234")

    st.markdown("</div></div>", unsafe_allow_html=True)
    st.stop()

# -----------------------------
# NAVBAR
# -----------------------------

col1, col2, col3, col4, col5 = st.columns([3,1,1,1,1])

with col1:
    st.markdown("### 🤖 AI Ops Monitor")

with col2:
    if st.button("Dashboard"):
        st.session_state.page = "Dashboard"

with col3:
    if st.button("Billing"):
        st.session_state.page = "Billing"

with col4:
    if st.button("Settings"):
        st.session_state.page = "Settings"

with col5:
    if st.button("Logout"):
        st.session_state.logged_in = False
        st.rerun()

st.divider()

# -----------------------------
# ROUTER
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
