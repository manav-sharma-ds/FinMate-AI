import streamlit as st


def page_header(title, subtitle=None, back_target="🏠 Dashboard", back_label="Dashboard"):

    back_col, _ = st.columns([0.22, 0.78])

    with back_col:

        if st.button(
            f"← {back_label}",
            key=f"back_link_{back_target}",
            use_container_width=True,
            type="secondary"
        ):
            st.session_state["pending_nav"] = back_target
            st.rerun()

    st.write("")

    st.markdown(
        f'<div class="fm-page-title">{title}</div>',
        unsafe_allow_html=True
    )

    if subtitle:

        st.markdown(
            f'<div class="fm-page-subtitle">{subtitle}</div>',
            unsafe_allow_html=True
        )