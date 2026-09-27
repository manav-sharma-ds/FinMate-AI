import pandas as pd
from sklearn.ensemble import IsolationForest


def detect_anomalies(df):



    if df.empty or len(df) < 5:
        return df

    model = IsolationForest(
        contamination=0.1,
        random_state=42
    )

    model.fit(df[["amount"]])

    df = df.copy()

    df["anomaly"] = model.predict(
        df[["amount"]]
    )

    df["risk"] = df["anomaly"].apply(
        lambda x: "Unusual" if x == -1 else "Normal"
    )

    return df