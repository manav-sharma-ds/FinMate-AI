import streamlit as st

from landing import landing
from auth import auth_page
from components.sidebar import sidebar

from modules.dashboard import dashboard_page
from modules.ai_advisor import ai_advisor_page
from modules.budget import budget_page
from modules.expense import expense_page
from modules.investment import investment_page
from modules.reports import reports_page
from modules.settings import settings_page


# ==================================================
# PAGE CONFIG
# ==================================================

st.set_page_config(
    page_title="FinMate AI",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==================================================
# SESSION STATE
# ==================================================

if "show_login" not in st.session_state:
    st.session_state.show_login = False

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False


# ==================================================
# GLOBAL THEME
# Loaded from styles/style.css — the single authoritative
# stylesheet for the whole app. Do not add global CSS here;
# add it to styles/style.css instead.
# ==================================================

with open("styles/style.css") as css_file:
    st.markdown(
        f"<style>{css_file.read()}</style>",
        unsafe_allow_html=True
    )


# ==================================================
# ROUTING
# ==================================================

if st.session_state.logged_in:

    page = sidebar()

    if page == "🏠 Dashboard":
        dashboard_page()

    elif page == "🤖 AI Advisor":
        ai_advisor_page()

    elif page == "💰 Budget Planner":
        budget_page()

    elif page == "💳 Expense Tracker":
        expense_page()

    elif page == "📈 Investment Analyzer":
        investment_page()

    elif page == "📄 Reports":
        reports_page()

    elif page == "⚙️ Settings":
        settings_page()


elif st.session_state.show_login:

    auth_page()


else:

    landing()