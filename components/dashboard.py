import streamlit as st

from charts.finance_chart import income_expense_chart
from models.financial_engine import calculate_savings


# ==================================================
# KPI CARD
# ==================================================

def card(title, value, icon):

    st.markdown(
        f"""<div class="fm-kpi-card">
<div class="fm-kpi-top">
<div class="fm-kpi-icon">{icon}</div>
<div class="fm-kpi-title">{title}</div>
</div>
<div class="fm-kpi-value">{value}</div>
</div>""",
        unsafe_allow_html=True
    )


# ==================================================
# DASHBOARD
# ==================================================

def dashboard_page():

    st.markdown("""
<style>

.dashboard-heading {
    color: #0F172A;
    font-size: 38px;
    font-weight: 750;
    letter-spacing: -1px;
    margin-bottom: 3px;
}

.dashboard-subtitle {
    color: #64748B;
    font-size: 16px;
    margin-bottom: 30px;
}


/* KPI CARDS */

.fm-kpi-card {
    background: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-radius: 16px;
    padding: 22px;
    min-height: 125px;
    box-shadow: 0 5px 18px rgba(15, 23, 42, 0.045);
    transition: 0.2s ease;
}

.fm-kpi-card:hover {
    border-color: #BBF7D0;
    box-shadow: 0 8px 25px rgba(15, 23, 42, 0.07);
}

.fm-kpi-top {
    display: flex;
    align-items: center;
    gap: 9px;
    margin-bottom: 14px;
}

.fm-kpi-icon {
    font-size: 18px;
}

.fm-kpi-title {
    color: #64748B;
    font-size: 14px;
    font-weight: 600;
}

.fm-kpi-value {
    color: #0F172A;
    font-size: 30px;
    font-weight: 750;
    letter-spacing: -0.5px;
}


/* SECTION HEADINGS */

.section-heading {
    color: #0F172A;
    font-size: 22px;
    font-weight: 700;
    margin-bottom: 15px;
}


/* HEALTH CARD */

.health-card {
    background: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-radius: 16px;
    padding: 24px;
    min-height: 155px;
    box-shadow: 0 5px 18px rgba(15, 23, 42, 0.045);
}

.health-label {
    color: #64748B;
    font-size: 14px;
    font-weight: 600;
    margin-bottom: 10px;
}

.health-value {
    color: #0F172A;
    font-size: 34px;
    font-weight: 750;
}

.health-description {
    color: #94A3B8;
    font-size: 13px;
    margin-top: 7px;
}

.health-score {
    color: #15803D;
    font-size: 28px;
    font-weight: 750;
}

.health-status {
    color: #64748B;
    font-size: 13px;
    margin-top: 5px;
}


/* PROGRESS */

.stProgress > div > div > div {
    background: #16A34A !important;
}


/* PLOTLY */

div[data-testid="stPlotlyChart"] {
    background: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-radius: 16px;
    padding: 10px;
    box-shadow: 0 5px 18px rgba(15, 23, 42, 0.045);
}

</style>
""", unsafe_allow_html=True)


    # ==================================================
    # DATA
    # ==================================================

    data = calculate_savings()

    income = data["income"]
    budget = data["budget"]
    expenses = data["expenses"]
    savings = data["savings"]


    # ==================================================
    # HEADER
    # ==================================================

    st.markdown(
        """<div class="dashboard-heading">Financial Dashboard</div>
<div class="dashboard-subtitle">
Monitor your financial health and spending in one place.
</div>""",
        unsafe_allow_html=True
    )


    # ==================================================
    # KPI CARDS
    # ==================================================

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        card("Income", f"₹{income:,.0f}", "💰")

    with c2:
        card("Budget", f"₹{budget:,.0f}", "💳")

    with c3:
        card("Expenses", f"₹{expenses:,.0f}", "💸")

    with c4:
        card("Savings", f"₹{savings:,.0f}", "🏦")


    st.write("")
    st.write("")


    # ==================================================
    # FINANCIAL OVERVIEW
    # ==================================================

    left, right = st.columns([2, 1], gap="large")

    with left:

        st.markdown(
            """<div class="section-heading">
Financial Overview
</div>""",
            unsafe_allow_html=True
        )

        st.plotly_chart(
            income_expense_chart(),
            use_container_width=True
        )


    # ==================================================
    # FINANCIAL HEALTH
    # ==================================================

    with right:

        st.markdown(
            """<div class="section-heading">
Financial Health
</div>""",
            unsafe_allow_html=True
        )

        if income == 0:

            st.warning(
                "Please create a budget first."
            )

        else:

            expense_ratio = (
                expenses / income
            ) * 100

            savings_ratio = (
                savings / income
            ) * 100

            budget_ratio = (
                budget / income
            ) * 100


            expense_score = max(
                0,
                100 - expense_ratio
            )

            savings_score = min(
                savings_ratio * 2,
                100
            )

            budget_score = min(
                budget_ratio,
                100
            )


            health_score = (
                (expense_score * 0.4)
                + (savings_score * 0.4)
                + (budget_score * 0.2)
            )

            health_score = min(
                max(health_score, 0),
                100
            )


            if health_score >= 75:

                health_status = "Strong financial position"

            elif health_score >= 50:

                health_status = "Moderate financial position"

            else:

                health_status = "Needs improvement"


            st.markdown(
                f"""<div class="health-card">
<div class="health-label">Financial Health Score</div>
<div class="health-score">{health_score:.0f} / 100</div>
<div class="health-status">{health_status}</div>
</div>""",
                unsafe_allow_html=True
            )


            st.write("")


            st.markdown(
                f"""<div class="health-card">
<div class="health-label">Expense Ratio</div>
<div class="health-value">{expense_ratio:.1f}%</div>
<div class="health-description">
Percentage of income spent on expenses
</div>
</div>""",
                unsafe_allow_html=True
            )


            st.write("")


            st.progress(
                min(int(expense_ratio), 100)
            )