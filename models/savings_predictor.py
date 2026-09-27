import pandas as pd
from sklearn.ensemble import RandomForestRegressor


def predict_savings(income, expenses):

    data = pd.DataFrame({
        "income": [income],
        "expenses": [expenses]
    })

    savings = income - expenses

    model = RandomForestRegressor(
        n_estimators=100,
        random_state=42
    )

    training_data = pd.DataFrame({
        "income": [30000, 40000, 50000, 60000, 70000],
        "expenses": [25000, 30000, 35000, 42000, 48000],
        "savings": [5000, 10000, 15000, 18000, 22000]
    })

    model.fit(
        training_data[["income", "expenses"]],
        training_data["savings"]
    )

    prediction = model.predict(
        data[["income", "expenses"]]
    )[0]

    return round(prediction, 2)