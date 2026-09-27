import streamlit as st

from database.database import create_user, login_user
from auth import verify_password


def login():

    st.markdown("""
    <style>

    .stApp{
        background:#0F172A;
    }

    .box{
        max-width:450px;
        margin:auto;
        margin-top:70px;
        background:#1E293B;
        padding:40px;
        border-radius:18px;
        border:1px solid rgba(255,255,255,.08);
    }

    .title{
        text-align:center;
        font-size:42px;
        font-weight:700;
        color:#22c55e;
    }

    .sub{
        text-align:center;
        color:#94A3B8;
        margin-bottom:30px;
    }

    </style>
    """, unsafe_allow_html=True)

    tab1, tab2 = st.tabs(["Sign In", "Create Account"])

    # ================= SIGN IN ================= #

    with tab1:

        st.markdown("<div class='box'>", unsafe_allow_html=True)

        st.markdown("<div class='title'>FinMate AI</div>", unsafe_allow_html=True)

        st.markdown("<div class='sub'>Welcome Back</div>", unsafe_allow_html=True)

        email = st.text_input(
            "Email",
            key="login_email"
        )

        password = st.text_input(
            "Password",
            type="password",
            key="login_password"
        )

        if st.button(
            "Sign In",
            use_container_width=True
        ):

            user = login_user(email)

            if user:

                if verify_password(password, user[3]):

                    st.session_state.logged_in = True
                    st.session_state.user = user[1]
                    st.session_state.email = user[2]

                    st.rerun()

                else:

                    st.error("Incorrect password.")

            else:

                st.error("Account not found.")

        st.markdown("</div>", unsafe_allow_html=True)

    # ================= SIGN UP ================= #

    with tab2:

        st.markdown("<div class='box'>", unsafe_allow_html=True)

        st.markdown("<div class='title'>Create Account</div>", unsafe_allow_html=True)

        st.markdown("<div class='sub'>Join FinMate AI</div>", unsafe_allow_html=True)

        name = st.text_input(
            "Full Name"
        )

        email = st.text_input(
            "Email Address"
        )

        password = st.text_input(
            "Create Password",
            type="password"
        )

        confirm = st.text_input(
            "Confirm Password",
            type="password"
        )

        if st.button(
            "Create Account",
            use_container_width=True
        ):

            if password != confirm:

                st.error("Passwords do not match.")

            elif len(password) < 6:

                st.error("Password must be at least 6 characters.")

            else:

                ok = create_user(
                    name,
                    email,
                    password
                )

                if ok:

                    st.success(
                        "Account created successfully. You can now sign in."
                    )

                else:

                    st.error(
                        "Email already exists."
                    )

        st.markdown("</div>", unsafe_allow_html=True)