import streamlit as st


def hero():

    st.markdown("""
    <div style="text-align:center;padding:80px 0 40px 0;">

        <div style="
        font-size:72px;
        font-weight:800;
        color:white;
        line-height:1.1;
        ">

        AI-Powered <span style="color:#22c55e;">Financial</span><br>
        Assistant for India

        </div>

        <br>

        <div style="
        color:#94A3B8;
        font-size:22px;
        max-width:850px;
        margin:auto;
        line-height:1.7;
        ">

        Plan budgets, track expenses, analyze investments,
        and get intelligent financial guidance using AI.

        </div>

    </div>
    """, unsafe_allow_html=True)

    c1, c2, c3 = st.columns([2,2,2])

    with c2:
        st.button(
            "Get Started Free",
            use_container_width=True,
            type="primary"
        ) 