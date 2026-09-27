
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

df = pd.read_csv("data/financial_data.csv")

features = [
    "age",
    "gender",
    "education_level",
    "employment_status",
    "monthly_income_usd",
    "savings_usd",
    "has_loan",
    "loan_amount_usd",
    "loan_term_months",
    "monthly_emi_usd",
    "loan_interest_rate_pct",
    "debt_to_income_ratio",
    "credit_score",
    "savings_to_income_ratio",
    "region"
]

X = df[features]
y = df["monthly_expenses_usd"]

categorical_features = [
    "gender",
    "education_level",
    "employment_status",
    "has_loan",
    "region"
]

preprocessor = ColumnTransformer(
    transformers=[
        (
            "categorical",
            OneHotEncoder(handle_unknown="ignore"),
            categorical_features
        )
    ],
    remainder="passthrough"
)

model = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        ("model", RandomForestRegressor(
            n_estimators=100,
            random_state=42
        ))
    ]
)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model.fit(X_train, y_train)

predictions = model.predict(X_test)

mae = mean_absolute_error(y_test, predictions)
rmse = mean_squared_error(y_test, predictions) ** 0.5
r2 = r2_score(y_test, predictions)

print("Expense Prediction Model")
print("------------------------")
print("Training Records:", len(X_train))
print("Testing Records:", len(X_test))
print("MAE:", round(mae, 2))
print("RMSE:", round(rmse, 2))
print("R2 Score:", round(r2, 4))

joblib.dump(model, "models/expense_prediction_model.pkl")

print("Model saved successfully!")
