import streamlit as st
from components.page_header import page_header


def settings_page():

    page_header(
        "Settings",
        "Manage your profile and application preferences.",
        back_target="🏠 Dashboard"
    )

    st.markdown(
        '<div class="fm-section-heading">Profile</div>',
        unsafe_allow_html=True
    )

    name = st.text_input("Name", "Manav Sharma")

    email = st.text_input("Email", "admin@finmate.ai")

    st.divider()

    st.markdown(
        '<div class="fm-section-heading">Preferences</div>',
        unsafe_allow_html=True
    )

    currency = st.selectbox(
        "Currency",
        ["INR (₹)", "USD ($)", "EUR (€)"]
    )

    theme = st.selectbox(
        "Theme",
        ["Dark", "Light"]
    )

    notifications = st.toggle(
        "Enable Notifications",
        value=True
    )

    if st.button(
        "Save Settings",
        use_container_width=True,
        type="primary"
    ):
        st.success("Settings saved successfully.")