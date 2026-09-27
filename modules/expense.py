import streamlit as st
from database.database import conn
import pandas as pd

from models.anomaly_detector import detect_anomalies
from services.groq_ai import explain_spending_risk
from components.page_header import page_header


def expense_page():

    page_header(
        "Expense Tracker",
        "Record and review your daily spending.",
        back_target="🏠 Dashboard"
    )

    # =========================
    # ADD EXPENSE
    # =========================

    st.markdown(
        '<div class="fm-section-heading">Add an Expense</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2, gap="large")

    with col1:
        category = st.selectbox(
            "Category",
            [
                "Food",
                "Shopping",
                "Fuel",
                "Bills",
                "Entertainment",
                "Travel",
                "Healthcare",
                "Other"
            ]
        )

    with col2:
        amount = st.number_input(
            "Amount (₹)",
            min_value=0.0,
            step=100.0
        )

    if st.button(
        "Add Expense",
        use_container_width=True,
        type="primary"
    ):

        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO expenses(category, amount)
            VALUES(?,?)
            """,
            (category, amount)
        )

        conn.commit()

        st.success("Expense added successfully.")

    st.divider()

    # =========================
    # EXPENSE HISTORY
    # =========================

    st.markdown(
        '<div class="fm-section-heading">Expense History</div>',
        unsafe_allow_html=True
    )

    df = pd.read_sql(
        "SELECT * FROM expenses ORDER BY id DESC",
        conn
    )

    if not df.empty:

        analyzed_df = detect_anomalies(df)

        if "risk" in analyzed_df.columns:

            display_df = analyzed_df[
                ["id", "category", "amount", "risk"]
            ].copy()

            display_df["amount"] = display_df["amount"].apply(
                lambda x: f"₹{x:,.0f}"
            )

            st.dataframe(
                display_df,
                use_container_width=True,
                hide_index=True
            )

            unusual_count = (
                analyzed_df["risk"] == "Unusual"
            ).sum()

            if unusual_count > 0:

                st.warning(
                    f"{unusual_count} unusual spending transaction(s) detected."
                )

                unusual_transactions = analyzed_df[
                    analyzed_df["risk"] == "Unusual"
                ][["category", "amount"]]

                if st.button(
                    "Explain Spending Risk",
                    use_container_width=True,
                    type="secondary"
                ):

                    with st.spinner("Analyzing spending pattern..."):

                        explanation = explain_spending_risk(
                            unusual_transactions.to_string(index=False)
                        )

                    st.info(explanation)

            else:

                st.success(
                    "No unusual spending patterns detected."
                )

        else:

            st.info(
                "Add at least 5 expenses to perform spending risk analysis."
            )

        st.write("")

        total = df["amount"].sum()

        st.metric(
            "Total Expenses",
            f"₹{total:,.0f}"
        )

    else:

        st.info("No expenses added yet.")