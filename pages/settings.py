import streamlit as st

def render():

    st.title("⚙️ Settings")

    theme = st.selectbox(
        "Choose Theme",
        ["Dark", "Light", "Rainbow"],
        index=["Dark","Light","Rainbow"].index(st.session_state.theme)
    )

    if theme != st.session_state.theme:
        st.session_state.theme = theme
        st.rerun()

    st.success(f"{theme} Mode Activated")
