import streamlit as st

def render():

    st.title("⚙️ Settings")

    theme_choice = st.selectbox(
        "Choose Theme",
        ["Dark", "Light", "Rainbow"],
        index=["Dark","Light","Rainbow"].index(st.session_state.theme)
    )

    if theme_choice != st.session_state.theme:
        st.session_state.theme = theme_choice
        st.rerun()

    st.success(f"{st.session_state.theme} mode activated 🌈")
