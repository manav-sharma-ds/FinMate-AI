import streamlit as st
from database.database import conn
from components.page_header import page_header


def budget_page():

    page_header(
        "Budget Planner",
        "Set your monthly income and create a spending budget that works for you.",
        back_target="🏠 Dashboard"
    )

    # =========================
    # BUDGET FORM
    # =========================

    st.markdown(
        '<div class="fm-section-heading">Set Your Monthly Budget</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2, gap="large")

    with col1:
        income = st.number_input(
            "Monthly Income",
            min_value=0.0,
            step=1000.0,
            format="%.0f"
        )

    with col2:
        budget = st.number_input(
            "Monthly Budget",
            min_value=0.0,
            step=1000.0,
            format="%.0f"
        )

    st.write("")

    if st.button(
        "Save Budget",
        use_container_width=True,
        type="primary"
    ):

        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO budget(income, budget)
            VALUES(?, ?)
            """,
            (income, budget)
        )

        conn.commit()

        st.success("Budget saved successfully.")

    st.divider()

    # =========================
    # CURRENT BUDGET
    # =========================

    st.markdown(
        '<div class="fm-section-heading">Current Budget</div>',
        unsafe_allow_html=True
    )

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT income, budget
        FROM budget
        ORDER BY id DESC
        LIMIT 1
        """
    )

    row = cursor.fetchone()

    # =========================
    # BUDGET SUMMARY
    # =========================

    if row:

        col1, col2 = st.columns(2, gap="large")

        with col1:
            st.markdown(
                f"""<div class="fm-kpi-card">
<div class="fm-kpi-title">Monthly Income</div>
<div class="fm-kpi-value">₹{row[0]:,.0f}</div>
</div>""",
                unsafe_allow_html=True
            )

        with col2:
            st.markdown(
                f"""<div class="fm-kpi-card">
<div class="fm-kpi-title">Monthly Budget</div>
<div class="fm-kpi-value">₹{row[1]:,.0f}</div>
</div>""",
                unsafe_allow_html=True
            )

    else:

        st.info(
            "No budget has been created yet. Enter your monthly income and budget above."
        )

    # =========================
    # WHAT-IF FINANCIAL SIMULATOR
    # =========================

    st.divider()

    st.markdown(
        '<div class="fm-section-heading">What-If Financial Simulator</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="fm-page-subtitle">
        Explore how changes in your income and expenses could affect your monthly savings.
        </div>
        """,
        unsafe_allow_html=True
    )

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT COALESCE(SUM(amount), 0)
        FROM expenses
        """
    )

    expense_row = cursor.fetchone()

    current_expenses = float(expense_row[0]) if expense_row else 0.0

    current_income = float(row[0]) if row else 0.0

    if current_income > 0:

        st.write("")

        col1, col2 = st.columns(2, gap="large")

        with col1:

            expense_change = st.slider(
                "Change Monthly Expenses (%)",
                min_value=-50,
                max_value=50,
                value=0,
                step=5
            )

        with col2:

            income_change = st.slider(
                "Change Monthly Income (%)",
                min_value=-30,
                max_value=30,
                value=0,
                step=5
            )

        new_income = current_income * (1 + income_change / 100)

        new_expenses = current_expenses * (1 + expense_change / 100)

        current_savings = current_income - current_expenses

        new_savings = new_income - new_expenses

        current_savings_rate = (
            (current_savings / current_income) * 100
            if current_income > 0
            else 0
        )

        new_savings_rate = (
            (new_savings / new_income) * 100
            if new_income > 0
            else 0
        )

        savings_difference = new_savings - current_savings

        annual_savings_difference = savings_difference * 12

        st.write("")

        st.markdown(
            '<div class="fm-section-heading">Simulation Result</div>',
            unsafe_allow_html=True
        )

        result1, result2, result3, result4 = st.columns(4)

        with result1:
            st.metric(
                "Projected Income",
                f"₹{new_income:,.0f}",
                f"{income_change:+d}%"
            )

        with result2:
            st.metric(
                "Projected Expenses",
                f"₹{new_expenses:,.0f}",
                f"{expense_change:+d}%"
            )

        with result3:
            st.metric(
                "Projected Savings",
                f"₹{new_savings:,.0f}",
                f"₹{savings_difference:+,.0f}"
            )

        with result4:
            st.metric(
                "Savings Rate",
                f"{new_savings_rate:.1f}%",
                f"{new_savings_rate - current_savings_rate:+.1f}%"
            )

        st.write("")

        if savings_difference > 0:

            st.success(
                f"This scenario could increase your monthly savings by "
                f"₹{savings_difference:,.0f}, or approximately "
                f"₹{annual_savings_difference:,.0f} annually."
            )

        elif savings_difference < 0:

            st.warning(
                f"This scenario could reduce your monthly savings by "
                f"₹{abs(savings_difference):,.0f}, or approximately "
                f"₹{abs(annual_savings_difference):,.0f} annually."
            )

        else:

            st.info(
                "This scenario does not change your projected monthly savings."
            )

    else:

        st.info(
            "Create a monthly budget first to use the What-If Financial Simulator."
        )