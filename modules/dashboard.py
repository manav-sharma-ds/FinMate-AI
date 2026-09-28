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

.health-card {
    background: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-radius: 16px;
    padding: 22px;
    min-height: 145px;
    box-shadow: 0 5px 18px rgba(15, 23, 42, 0.045);
}

.health-label {
    color: #64748B;
    font-size: 13px;
    font-weight: 650;
    text-transform: uppercase;
    letter-spacing: 0.4px;
    margin-bottom: 10px;
}

.health-value {
    color: #0F172A;
    font-size: 30px;
    font-weight: 750;
}

.health-description {
    color: #94A3B8;
    font-size: 13px;
    margin-top: 6px;
}

.health-score {
    font-size: 28px;
    font-weight: 750;
}

.health-status {
    color: #64748B;
    font-size: 13px;
    margin-top: 5px;
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
        """<div class="fm-page-title">Financial Dashboard</div>
<div class="fm-page-subtitle">
Monitor your financial health and spending in one place.
</div>""",
        unsafe_allow_html=True
    )


    # ==================================================
    # KPI CARDS
    # ==================================================

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        card(
            "Income",
            f"₹{income:,.0f}",
            "💰"
        )

    with c2:
        card(
            "Budget",
            f"₹{budget:,.0f}",
            "💳"
        )

    with c3:
        card(
            "Expenses",
            f"₹{expenses:,.0f}",
            "💸"
        )

    with c4:
        card(
            "Savings",
            f"₹{savings:,.0f}",
            "🏦"
        )


    st.write("")
    st.write("")


    # ==================================================
    # FINANCIAL OVERVIEW
    # ==================================================

    left, right = st.columns(
        [2, 1],
        gap="large"
    )

    with left:

        st.markdown(
            '<div class="fm-section-heading">Financial Overview</div>',
            unsafe_allow_html=True
        )

        st.plotly_chart(
            income_expense_chart(),
            use_container_width=True
        )


    # ==================================================
    # FINANCIAL HEALTH PROFILE
    # ==================================================

    with right:

        st.markdown(
            '<div class="fm-section-heading">Financial Health Profile</div>',
            unsafe_allow_html=True
        )

        if income == 0:

            st.warning(
                "Please create a budget first."
            )

        else:

            expense_ratio = (expenses / income) * 100

            savings_ratio = (savings / income) * 100

            budget_ratio = (
                (budget / income) * 100
                if income > 0
                else 0
            )

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

            if savings_ratio >= 20:
                savings_status = "Healthy savings rate"
            elif savings_ratio >= 10:
                savings_status = "Moderate savings rate"
            else:
                savings_status = "Low savings rate"

            if expense_ratio <= 50:
                expense_status = "Controlled spending"
            elif expense_ratio <= 75:
                expense_status = "Moderate spending"
            else:
                expense_status = "High spending"

            if budget > 0 and expenses <= budget:
                budget_status = "Within budget"
            else:
                budget_status = "Budget exceeded"

            if health_status == "Strong financial position":
                status_class = "fm-badge-success"
            elif health_status == "Moderate financial position":
                status_class = "fm-badge-warning"
            else:
                status_class = "fm-badge-danger"

            st.markdown(
                f"""<div class="health-card">
<div class="health-label">Financial Health Score</div>
<div class="health-score {status_class}">{health_score:.0f} / 100</div>
<div class="health-status">{health_status}</div>
</div>""",
                unsafe_allow_html=True
            )

            st.write("")

            st.markdown(
                f"""<div class="health-card">
<div class="health-label">Savings Rate</div>
<div class="health-value">{savings_ratio:.1f}%</div>
<div class="health-description">
{savings_status}
</div>
</div>""",
                unsafe_allow_html=True
            )

            st.write("")

            st.markdown(
                f"""<div class="health-card">
<div class="health-label">Expense Ratio</div>
<div class="health-value">{expense_ratio:.1f}%</div>
<div class="health-description">
{expense_status}
</div>
</div>""",
                unsafe_allow_html=True
            )

            st.write("")

            budget_utilization = (
                (expenses / budget) * 100
                if budget > 0
                else 0
            )

            st.markdown(
                f"""<div class="health-card">
<div class="health-label">Budget Status</div>
<div class="health-value" style="font-size:22px;">
{budget_status}
</div>
<div class="health-description">
Budget utilization: {budget_utilization:.1f}%
</div>
</div>""",
                unsafe_allow_html=True
            )

            st.write("")

            st.progress(
                min(int(budget_utilization), 100)
            )