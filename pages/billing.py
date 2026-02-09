import streamlit as st

def render():

    st.title("💳 Billing & Subscription")

    st.subheader("Current Plan: Growth")
    st.success("Your subscription is active.")

    st.divider()

    st.subheader("Upgrade Plan")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Upgrade to Enterprise"):
            st.info("Redirecting to payment gateway...")

    with col2:
        if st.button("Downgrade to Starter"):
            st.warning("Plan will change next billing cycle.")
