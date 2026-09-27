from services.expense_predictor import predict_expenses

data = {
    "age": 25,
    "gender": "Male",
    "education_level": "Bachelor's",
    "employment_status": "Employed",
    "monthly_income_usd": 4000,
    "savings_usd": 10000,
    "has_loan": "No",
    "loan_amount_usd": 0,
    "loan_term_months": 0,
    "monthly_emi_usd": 0,
    "loan_interest_rate_pct": 0,
    "debt_to_income_ratio": 0,
    "credit_score": 700,
    "savings_to_income_ratio": 2.5,
    "region": "North"
}

prediction = predict_expenses(data)

print("Predicted Monthly Expenses:", prediction)