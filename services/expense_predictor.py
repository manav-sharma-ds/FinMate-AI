import joblib
import pandas as pd

model = joblib.load("models/expense_prediction_model.pkl")


def predict_expenses(data):
    df = pd.DataFrame([data])

    prediction = model.predict(df)[0]

    return round(prediction, 2)