import streamlit as st
import requests

API_URL = "https://your-backend-url.com"

if "token" not in st.session_state:
    st.session_state.token = None

st.title("AI Ops SaaS")

if not st.session_state.token:

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        res = requests.post(
            f"{API_URL}/login",
            params={"email": email, "password": password}
        )

        if res.status_code == 200:
            st.session_state.token = res.json()["access_token"]
            st.success("Logged In")
            st.rerun()
        else:
            st.error("Login Failed")

else:
    st.success("Dashboard Access Granted")

    if st.button("Upgrade to Pro"):

        res = requests.post(
            f"{API_URL}/create-checkout",
            params={
                "email": "user@email.com",
                "price_id": "price_123456"
            }
        )

        checkout_url = res.json()["url"]
        st.markdown(f"[Click here to Pay]({checkout_url})")
