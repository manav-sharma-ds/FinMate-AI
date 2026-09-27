import streamlit as st


def sidebar():

    if "pending_nav" in st.session_state:
        st.session_state["main_nav"] = st.session_state["pending_nav"]
        del st.session_state["pending_nav"]

    st.markdown("""
    <style>

    section[data-testid="stSidebar"] {
        background: #FFFFFF;
        border-right: 1px solid #E4E7EC;
    }

    section[data-testid="stSidebar"] > div {
        padding-top: 1.5rem;
    }

    .sidebar-subtitle {
        text-align: center;
        color: #94A0AE;
        font-size: 12.5px;
        margin-top: 4px;
        margin-bottom: 22px;
    }

    section[data-testid="stSidebar"] .stRadio > label {
        color: #5B6472 !important;
        font-size: 12.5px !important;
        font-weight: 650 !important;
        text-transform: uppercase;
        letter-spacing: 0.4px;
    }

    section[data-testid="stSidebar"] .stRadio div[role="radiogroup"] {
        gap: 4px;
    }

    section[data-testid="stSidebar"] .stRadio div[role="radiogroup"] label {
        position: relative;
        border-radius: 8px;
        padding: 9px 10px 9px 14px;
        color: #475569;
        font-size: 14.5px;
        transition: 0.15s;
    }

    section[data-testid="stSidebar"] .stRadio div[role="radiogroup"] label:hover {
        background: #EEF2FF;
        color: #4F46E5;
    }

    section[data-testid="stSidebar"]
    .stRadio div[role="radiogroup"]
    label:has(input:checked) {
        background: #EEF2FF;
        color: #4F46E5 !important;
        font-weight: 650;
    }

    section[data-testid="stSidebar"]
    .stRadio div[role="radiogroup"]
    label:has(input:checked)::before {
        content: "";
        position: absolute;
        left: 0;
        top: 8px;
        bottom: 8px;
        width: 3px;
        border-radius: 3px;
        background: #4F46E5;
    }

    section[data-testid="stSidebar"]
    .stRadio div[role="radiogroup"] label > div:first-child {
        display: none;
    }

    .logged-in {
        background: #F0FDF4;
        border: 1px solid #DCFCE7;
        color: #15803D;
        border-radius: 9px;
        padding: 10px 14px;
        text-align: center;
        font-size: 13.5px;
        font-weight: 650;
        margin-bottom: 10px;
    }

    section[data-testid="stSidebar"] .stButton button {
        background: #FFFFFF !important;
        color: #475569 !important;
        border: 1px solid #C9CED6 !important;
    }

    section[data-testid="stSidebar"] .stButton button:hover {
        background: #FEF2F2 !important;
        border-color: #FCA5A5 !important;
        color: #DC2626 !important;
    }

    </style>
    """, unsafe_allow_html=True)


    st.sidebar.markdown(
        '<div class="fm-wordmark" style="text-align:center; font-size:22px;">'
        'FinMate<span class="fm-wordmark-badge">AI</span></div>'
        '<div class="sidebar-subtitle">Personal Finance Platform</div>',
        unsafe_allow_html=True
    )


    st.sidebar.divider()


    page = st.sidebar.radio(
        "Navigation",
        [
            "🏠 Dashboard",
            "🤖 AI Advisor",
            "💰 Budget Planner",
            "💳 Expense Tracker",
            "📈 Investment Analyzer",
            "📄 Reports",
            "⚙️ Settings"
        ],
        key="main_nav"
    )


    st.sidebar.divider()


    st.sidebar.markdown("""
    <div class="logged-in">
        ● Logged In
    </div>
    """, unsafe_allow_html=True)


    if st.sidebar.button(
        "Logout",
        use_container_width=True,
        key="sidebar_logout",
        type="secondary"
    ):

        st.session_state.logged_in = False
        st.session_state.show_login = False
        st.rerun()


    return page