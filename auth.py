import streamlit as st


def auth_page():

    # =========================
    # AUTH PAGE - PAGE SPECIFIC STYLING
    # (inputs/buttons/wordmark come from the global stylesheet)
    # =========================

    st.markdown("""
    <style>

    .auth-page {
        padding-top: 55px;
    }

    .auth-title {
        text-align: center;
        color: #0B1220;
        font-size: 30px;
        font-weight: 750;
        letter-spacing: -0.7px;
        margin-top: 30px;
        margin-bottom: 8px;
    }

    .auth-subtitle {
        text-align: center;
        color: #5B6472;
        font-size: 15px;
        margin-bottom: 28px;
    }

    .auth-footer {
        text-align: center;
        color: #94A0AE;
        font-size: 12.5px;
        margin-top: 20px;
    }

    </style>
    """, unsafe_allow_html=True)


    # =========================
    # PAGE
    # =========================

    st.markdown(
        '<div class="auth-page"></div>',
        unsafe_allow_html=True
    )

    # Center everything
    left, center, right = st.columns([1, 1.05, 1])

    with center:

        # Logo
        st.markdown(
            '<div class="fm-wordmark" style="text-align:center; font-size:24px;">'
            'FinMate<span class="fm-wordmark-badge">AI</span></div>',
            unsafe_allow_html=True
        )

        # Heading
        st.markdown("""
        <div class="auth-title">
            Welcome back
        </div>

        <div class="auth-subtitle">
            Sign in to continue to your financial dashboard.
        </div>
        """, unsafe_allow_html=True)

        # Email
        email = st.text_input(
            "Email",
            placeholder="Enter your email",
            key="login_email"
        )

        # Password
        password = st.text_input(
            "Password",
            type="password",
            placeholder="Enter your password",
            key="login_password"
        )

        st.write("")

        # Sign In
        login = st.button(
            "Sign In",
            use_container_width=True,
            key="signin_button",
            type="primary"
        )

        # Login logic
        if login:

            if email == "admin@finmate.ai" and password == "123456":

                st.session_state.logged_in = True
                st.session_state.show_login = False
                st.rerun()

            else:

                st.error("Invalid email or password.")

        # Footer
        st.markdown("""
        <div class="auth-footer">
            Secure access to your personal finance dashboard.
        </div>
        """, unsafe_allow_html=True)