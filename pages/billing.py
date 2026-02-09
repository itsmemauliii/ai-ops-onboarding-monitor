import streamlit as st

def render():

    st.title("💳 Billing & Plans")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("Starter")
        st.write("$29/month")
        st.write("Basic analytics")
        st.button("Choose Starter")

    with col2:
        st.subheader("Growth")
        st.write("$99/month")
        st.write("Advanced analytics + alerts")
        st.button("Choose Growth")

    with col3:
        st.subheader("Enterprise")
        st.write("$299/month")
        st.write("Full AI monitoring suite")
        st.button("Choose Enterprise")
