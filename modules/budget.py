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