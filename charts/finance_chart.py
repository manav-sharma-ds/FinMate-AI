import plotly.graph_objects as go


def income_expense_chart():

    months = ["Jan","Feb","Mar","Apr","May","Jun"]

    income = [60000,65000,70000,75000,80000,85000]

    expenses = [30000,35000,40000,42000,45000,48000]

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=months,
            y=income,
            mode="lines+markers",
            name="Income"
        )
    )

    fig.add_trace(
        go.Scatter(
            x=months,
            y=expenses,
            mode="lines+markers",
            name="Expenses"
        )
    )

    fig.update_layout(
        template="plotly_dark",
        height=420,
        margin=dict(l=20,r=20,t=40,b=20)
    )

    return fig