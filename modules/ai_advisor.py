import streamlit as st

from models.financial_engine import calculate_savings
from services.groq_ai import ask_ai
from services.expense_predictor import predict_expenses
from models.anomaly_detector import detect_anomalies
from database.database import conn
import pandas as pd
from models.savings_predictor import predict_savings

USD_TO_INR = 95.8


def ai_advisor_page():

    # ==================================================
    # PAGE-SPECIFIC STYLING
    # (kpi cards, headings, chat, buttons come from the
    # global stylesheet)
    # ==================================================

    st.markdown("""
    <style>

    .advisor-card {
        background: #FFFFFF;
        border: 1px solid #E4E7EC;
        border-radius: 16px;
        padding: 22px;
        margin-top: 26px;
        margin-bottom: 22px;
        box-shadow: 0 5px 18px rgba(11, 18, 32, 0.04);
    }

    .advisor-title {
        color: #0B1220;
        font-size: 18px;
        font-weight: 700;
        margin-bottom: 8px;
    }

    .advisor-text {
        color: #5B6472;
        font-size: 14px;
        line-height: 1.7;
    }

    .prediction-card {
        background: #FFFFFF;
        border: 1px solid #E4E7EC;
        border-radius: 16px;
        padding: 24px;
        margin-bottom: 28px;
        box-shadow: 0 5px 18px rgba(11, 18, 32, 0.04);
    }

    .prediction-title {
        color: #0B1220;
        font-size: 18px;
        font-weight: 700;
        margin-bottom: 6px;
    }

    .prediction-text {
        color: #5B6472;
        font-size: 14px;
        margin-bottom: 18px;
    }

    .prediction-result {
        background: #EEF2FF;
        border: 1px solid #C7D2FE;
        border-radius: 12px;
        padding: 18px;
        margin-top: 18px;
    }

    .prediction-label {
        color: #4338CA;
        font-size: 13.5px;
        font-weight: 650;
        text-transform: uppercase;
        letter-spacing: 0.4px;
    }

    .prediction-value {
        color: #4338CA;
        font-size: 27px;
        font-weight: 750;
        margin-top: 4px;
    }

    .risk-card {
        background: #FFFFFF;
        border: 1px solid #E4E7EC;
        border-radius: 16px;
        padding: 22px;
        margin-top: 8px;
        box-shadow: 0 5px 18px rgba(11, 18, 32, 0.04);
    }

    </style>
    """, unsafe_allow_html=True)


    st.markdown(
        '<div class="fm-page-title">AI Financial Advisor</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="fm-page-subtitle">Get personalized financial guidance based on your current finances.</div>',
        unsafe_allow_html=True
    )


    financial_data = calculate_savings()

    income = financial_data["income"]
    budget = financial_data["budget"]
    expenses = financial_data["expenses"]
    savings_amount = financial_data["savings"]

    predicted_savings = predict_savings(
        income,
        expenses
    )


    c1, c2, c3, c4, c5 = st.columns(5)

    with c1:
        st.markdown(
            f'<div class="fm-kpi-card"><div class="fm-kpi-title">Income</div><div class="fm-kpi-value">₹{income:,.0f}</div></div>',
            unsafe_allow_html=True
        )

    with c2:
        st.markdown(
            f'<div class="fm-kpi-card"><div class="fm-kpi-title">Budget</div><div class="fm-kpi-value">₹{budget:,.0f}</div></div>',
            unsafe_allow_html=True
        )

    with c3:
        st.markdown(
            f'<div class="fm-kpi-card"><div class="fm-kpi-title">Expenses</div><div class="fm-kpi-value">₹{expenses:,.0f}</div></div>',
            unsafe_allow_html=True
        )

    with c4:
        st.markdown(
            f'<div class="fm-kpi-card"><div class="fm-kpi-title">Savings</div><div class="fm-kpi-value">₹{savings_amount:,.0f}</div></div>',
            unsafe_allow_html=True
        )

    with c5:
        st.markdown(
            f'<div class="fm-kpi-card"><div class="fm-kpi-title">Predicted Savings</div><div class="fm-kpi-value">₹{predicted_savings:,.0f}</div></div>',
            unsafe_allow_html=True
        )


    st.markdown(
        '<div class="advisor-card"><div class="advisor-title">Your Personal Financial Assistant</div>'
        '<div class="advisor-text">Ask questions about budgeting, saving, expenses, investments or your '
        'overall financial situation. FinMate AI will provide personalized guidance based on your '
        'financial information.</div></div>',
        unsafe_allow_html=True
    )


    st.markdown(
        '<div class="prediction-card">',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="prediction-title">Expense Prediction</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="prediction-text">Enter your financial details to estimate your monthly expenses using the FinMate AI prediction model.</div>',
        unsafe_allow_html=True
    )


    col1, col2 = st.columns(2, gap="large")


    with col1:

        age = st.number_input(
            "Age",
            min_value=18,
            max_value=100,
            value=25
        )

        monthly_income = st.number_input(
            "Monthly Income (₹)",
            min_value=0.0,
            value=40000.0,
            step=1000.0
        )

        savings = st.number_input(
            "Savings (₹)",
            min_value=0.0,
            value=100000.0,
            step=5000.0
        )

        credit_score = st.number_input(
            "Credit Score",
            min_value=300,
            max_value=850,
            value=700
        )


    with col2:

        gender = st.selectbox(
            "Gender",
            ["Male", "Female"]
        )

        education = st.selectbox(
            "Education Level",
            ["Bachelor's", "Master's", "High School", "PhD"]
        )

        employment = st.selectbox(
            "Employment Status",
            ["Employed", "Self-employed", "Unemployed", "Student"]
        )

        has_loan = st.selectbox(
            "Has Loan",
            ["No", "Yes"]
        )


    predict_button = st.button(
        "Predict Monthly Expenses",
        use_container_width=True,
        type="primary"
    )


    if predict_button:

        monthly_income_usd = monthly_income / USD_TO_INR
        savings_usd = savings / USD_TO_INR

        savings_ratio = (
            savings_usd / monthly_income_usd
            if monthly_income_usd > 0
            else 0
        )

        prediction_data = {
            "age": age,
            "gender": gender,
            "education_level": education,
            "employment_status": employment,
            "monthly_income_usd": monthly_income_usd,
            "savings_usd": savings_usd,
            "has_loan": has_loan,
            "loan_amount_usd": 0,
            "loan_term_months": 0,
            "monthly_emi_usd": 0,
            "loan_interest_rate_pct": 0,
            "debt_to_income_ratio": 0,
            "credit_score": credit_score,
            "savings_to_income_ratio": savings_ratio,
            "region": "North"
        }

        prediction = predict_expenses(prediction_data)

        prediction_inr = prediction * USD_TO_INR

        st.markdown(
            f"""
            <div class="prediction-result">
                <div class="prediction-label">
                    Predicted Monthly Expenses
                </div>
                <div class="prediction-value">
                    ₹{prediction_inr:,.2f}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )


    st.markdown("</div>", unsafe_allow_html=True)


    st.markdown(
        '<div class="fm-section-heading">Ask FinMate AI</div>',
        unsafe_allow_html=True
    )


    if "chat" not in st.session_state:
        st.session_state.chat = []


    for role, message in st.session_state.chat:

        with st.chat_message(role):
            st.markdown(message)


    user_prompt = st.chat_input(
        "Ask your financial advisor anything..."
    )


    if user_prompt:

        st.session_state.chat.append(
            ("user", user_prompt)
        )

        with st.chat_message("user"):
            st.markdown(user_prompt)


        financial_context = f"""
Current financial information from FinMate AI:

Monthly Income: ₹{income:,.0f}
Monthly Budget: ₹{budget:,.0f}
Total Expenses: ₹{expenses:,.0f}
Current Savings: ₹{savings_amount:,.0f}
Predicted Savings: ₹{predicted_savings:,.0f}
"""


        advisor_prompt = f"""
{financial_context}

User Question:
{user_prompt}

Use the financial information above when it is relevant.
Provide practical and personalized financial guidance.
Always express monetary values in Indian Rupees (₹).
Do not use dollars or USD unless the user specifically asks for another currency.
"""


        with st.chat_message("assistant"):

            with st.spinner("FinMate AI is thinking..."):

                answer = ask_ai(advisor_prompt)

            st.markdown(answer)


        st.session_state.chat.append(
            ("assistant", answer)
        )


    st.divider()

    st.markdown(
        '<div class="fm-section-heading">Spending Risk Analysis</div>',
        unsafe_allow_html=True
    )

    st.markdown('<div class="risk-card">', unsafe_allow_html=True)

    expense_df = pd.read_sql(
        "SELECT * FROM expenses ORDER BY id DESC",
        conn
    )

    if len(expense_df) >= 5:

        risk_df = detect_anomalies(expense_df)

        unusual = risk_df[
            risk_df["risk"] == "Unusual"
        ]

        if len(unusual) > 0:

            st.warning(
                f"{len(unusual)} unusual spending transaction(s) detected."
            )

            st.dataframe(
                unusual[["category", "amount"]],
                use_container_width=True,
                hide_index=True
            )

        else:

            st.success(
                "No unusual spending patterns detected."
            )

    else:

        st.info(
            "Add at least 5 expenses to generate spending risk analysis."
        )

    st.markdown("</div>", unsafe_allow_html=True)