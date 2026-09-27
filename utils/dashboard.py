import sqlite3
import pandas as pd
import plotly.express as px


# Connect to Database
conn = sqlite3.connect("database/finmate.db", check_same_thread=False)


# Load Expense Data
def load_expenses():
    query = "SELECT * FROM expenses"
    df = pd.read_sql(query, conn)
    return df


# Total Expense
def get_total_expense(df):
    return df["amount"].sum()


# Total Transactions
def get_total_transactions(df):
    return len(df)


# Category-wise Expense
def get_category_expense(df):
    return df.groupby("category")["amount"].sum().reset_index()

# Pie Chart
def expense_pie_chart(df):

    category_df = get_category_expense(df)

    fig = px.pie(
        category_df,
        names="category",
        values="amount",
        title="Expense Distribution"
    )

    return fig


# Bar Chart
def expense_bar_chart(df):

    category_df = get_category_expense(df)

    fig = px.bar(
        category_df,
        x="category",
        y="amount",
        color="category",
        title="Category-wise Expenses"
    )

    return fig