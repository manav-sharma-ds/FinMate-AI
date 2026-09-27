import streamlit as st
from components.page_header import page_header


def investment_page():

    page_header(
        "Investment Analyzer",
        "Estimate the future value of a monthly SIP investment.",
        back_target="🏠 Dashboard"
    )

    st.markdown(
        '<div class="fm-section-heading">Investment Details</div>',
        unsafe_allow_html=True
    )

    monthly = st.number_input(
        "Monthly SIP (₹)",
        min_value=500,
        value=5000,
        step=500
    )

    years = st.slider(
        "Investment Period (Years)",
        1,
        40,
        10
    )

    rate = st.slider(
        "Expected Annual Return (%)",
        1.0,
        20.0,
        12.0
    )

    r = rate / 100 / 12
    n = years * 12

    future_value = monthly * (((1 + r) ** n - 1) / r) * (1 + r)

    invested = monthly * n

    profit = future_value - invested

    st.write("")

    st.markdown(
        '<div class="fm-section-heading">Projected Outcome</div>',
        unsafe_allow_html=True
    )

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric(
            "Invested Amount",
            f"₹{invested:,.0f}"
        )

    with c2:
        st.metric(
            "Estimated Value",
            f"₹{future_value:,.0f}"
        )

    with c3:
        st.metric(
            "Estimated Profit",
            f"₹{profit:,.0f}"
        )

    st.write("")

    st.info(
        "This calculation is based on monthly compounding and is for estimation purposes only."
    )