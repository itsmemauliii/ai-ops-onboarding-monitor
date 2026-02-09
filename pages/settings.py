import streamlit as st

def render():

    st.title("💳 Billing & Plans")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("Starter")
        st.write("$29/month")
        st.write("Basic analytics")
        if st.button("Choose Starter"):
            st.success("Starter Activated")

    with col2:
        st.subheader("Growth")
        st.write("$99/month")
        st.write("Advanced analytics + alerts")
        if st.button("Choose Growth"):
            st.success("Growth Activated")

    with col3:
        st.subheader("Enterprise")
        st.write("$299/month")
        st.write("Full AI monitoring suite")
        if st.button("Choose Enterprise"):
            st.success("Enterprise Activated")
