from database.database import conn
import pandas as pd


def get_total_expenses():

    query = "SELECT SUM(amount) AS total FROM expenses"

    df = pd.read_sql(query, conn)

    total = df.iloc[0]["total"]

    if total is None:
        return 0

    return total


def get_latest_budget():

    query = """
    SELECT income,budget
    FROM budget
    ORDER BY id DESC
    LIMIT 1
    """

    df = pd.read_sql(query, conn)

    if df.empty:

        return 0,0

    return df.iloc[0]["income"],df.iloc[0]["budget"]


def calculate_savings():

    income,budget = get_latest_budget()

    expenses = get_total_expenses()

    savings = income-expenses

    return {

        "income":income,

        "budget":budget,

        "expenses":expenses,

        "savings":savings

    }