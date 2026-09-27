import streamlit as st


def navbar():

    # Navbar-specific styling only
    # (buttons and fonts come from the global stylesheet)
    st.markdown(
        """
        <style>
        .fm-menu-text {
            color: #5B6472;
            font-size: 15px;
            font-weight: 500;
            text-align: center;
            padding-top: 14px;
        }

        .fm-menu-text a {
            color: #5B6472;
            text-decoration: none;
            margin: 0 16px;
            transition: color 0.15s ease;
        }

        .fm-menu-text a:hover {
            color: #4F46E5;
        }

        @media (max-width: 900px) {
            .fm-menu-text {
                display: none;
            }
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Navbar layout
    col1, col2, col3 = st.columns([2.2, 5.5, 1.6])

    # Logo
    with col1:
        st.markdown(
            '<div class="fm-wordmark" style="font-size:24px; padding-top:8px;">'
            'FinMate<span class="fm-wordmark-badge">AI</span></div>',
            unsafe_allow_html=True
        )

    # Menu — real anchors to the sections on this page
    with col2:
        st.markdown(
            """
            <div class="fm-menu-text">
                <a href="#capabilities">Capabilities</a>
                <a href="#ai-advisor">AI Advisor</a>
            </div>
            """,
            unsafe_allow_html=True
        )

    # Button
    with col3:
        if st.button(
            "Get Started",
            key="navbar_get_started",
            use_container_width=True,
            type="primary"
        ):
            st.session_state.show_login = True
            st.rerun()

    st.markdown(
        """
        <div style="
            height:1px;
            background:#E4E7EC;
            margin-top:18px;
            margin-bottom:10px;
        "></div>
        """,
        unsafe_allow_html=True
    )
    