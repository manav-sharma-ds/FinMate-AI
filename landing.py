import streamlit as st
from components.navbar import navbar


def landing():

    # ==================================================
    # PAGE-SPECIFIC STYLING
    # ==================================================

    st.markdown("""
    <style>

    .hero {
        padding-top: 70px;
        padding-bottom: 60px;
    }

    .hero-eyebrow {
        color: #4F46E5;
        font-size: 13.5px;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 16px;
    }

    .hero-title {
        font-size: 58px;
        font-weight: 800;
        line-height: 1.1;
        letter-spacing: -1.6px;
        color: #0B1220;
        margin-bottom: 20px;
    }

    .hero-sub {
        color: #5B6472;
        font-size: 18px;
        line-height: 1.7;
        max-width: 640px;
        margin-bottom: 30px;
    }

    .hero-img {
        padding-top: 10px;
        text-align: center;
    }

    @media (max-width: 900px) {
        .hero-title {
            font-size: 40px;
            letter-spacing: -1px;
        }

        .hero-sub {
            font-size: 16px;
        }
    }

    .demo-wrapper {
        background: #FFFFFF;
        border: 1px solid #E4E7EC;
        border-radius: 16px;
        padding: 12px;
        box-shadow: 0 10px 30px rgba(11, 18, 32, 0.08);
    }

    /* ================= CAPABILITY LIST ================= */

    .fm-capability-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 0;
        max-width: 980px;
        margin: 0 auto;
    }

    @media (max-width: 900px) {
        .fm-capability-grid {
            grid-template-columns: 1fr;
        }
    }

    .fm-capability-row {
        padding: 22px 20px;
        border-bottom: 1px solid #E4E7EC;
    }

    .fm-capability-title {
        color: #0B1220;
        font-size: 16.5px;
        font-weight: 700;
        margin-bottom: 6px;
    }

    .fm-capability-desc {
        color: #5B6472;
        font-size: 14.5px;
        line-height: 1.6;
    }

    /* ================= AI ADVISOR SPOTLIGHT ================= */

    .fm-spotlight {
        background: #EEF2FF;
        border: 1px solid #C7D2FE;
        border-radius: 20px;
        padding: 48px 50px;
        margin-top: 55px;
        margin-bottom: 15px;
    }

    .fm-spotlight-eyebrow {
        color: #4338CA;
        font-size: 13px;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 12px;
    }

    .fm-spotlight-title {
        color: #0B1220;
        font-size: 28px;
        font-weight: 750;
        letter-spacing: -0.6px;
        margin-bottom: 12px;
    }

    .fm-spotlight-text {
        color: #4338CA;
        font-size: 15.5px;
        line-height: 1.7;
        max-width: 640px;
    }

    /* ================= FOOTER ================= */

    .fm-footer {
        text-align: center;
        color: #94A0AE;
        font-size: 13px;
        margin-top: 70px;
        padding-top: 24px;
        border-top: 1px solid #E4E7EC;
    }

    </style>
    """, unsafe_allow_html=True)


    # ==================================================
    # NAVBAR
    # ==================================================

    navbar()


    # ==================================================
    # HERO SECTION
    # ==================================================

    st.markdown('<div class="hero">', unsafe_allow_html=True)

    left, right = st.columns([1.15, 0.85], gap="large")

    with left:

        st.markdown(
            '<div class="hero-eyebrow">AI-Powered Personal Finance</div>',
            unsafe_allow_html=True
        )

        st.markdown("""
        <div class="hero-title">
            Understand your money.<br>
            Make better decisions.
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="hero-sub">
            FinMate AI brings budgeting, expense tracking, investment
            analysis and AI-driven financial guidance into one place,
            so you always know where you stand.
        </div>
        """, unsafe_allow_html=True)

        btn_col, _ = st.columns([0.34, 0.66])

        with btn_col:

            if st.button(
                "Get Started",
                use_container_width=True,
                key="landing_get_started",
                type="primary"
            ):

                st.session_state.show_login = True
                st.rerun()

    with right:

        st.markdown('<div class="hero-img">', unsafe_allow_html=True)

        st.image(
            "assets/images/hero.png",
            width=520
        )

        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)


    # ==================================================
    # CAPABILITIES SECTION
    # ==================================================

    st.markdown('<div id="capabilities"></div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="fm-section-title">
        Everything you need to manage your finances
    </div>

    <div class="fm-section-subtitle">
        One platform covering the full picture of your financial life —
        from daily spending to long-term investing.
    </div>
    """, unsafe_allow_html=True)

    capabilities = [
        ("Expense Tracking", "Log every transaction and see exactly where your money goes, by category and over time."),
        ("Budget Planning", "Set a monthly income and spending plan, and track how closely you stay within it."),
        ("Expense Prediction", "Estimate next month's likely expenses using a trained machine learning model."),
        ("Savings Prediction", "Project your expected savings based on your current income and spending pattern."),
        ("Investment Analysis", "Model the future value of a monthly SIP investment under different return scenarios."),
        ("AI Financial Advisor", "Ask questions about your finances and get guidance grounded in your real numbers."),
        ("Spending Risk Detection", "Automatically flag unusual transactions using anomaly detection."),
        ("Financial Reports", "Generate and download a clean summary of your financial position."),
    ]

    rows_html = ""

    for title, desc in capabilities:
        rows_html += (
            f'<div class="fm-capability-row">'
            f'<div class="fm-capability-title">{title}</div>'
            f'<div class="fm-capability-desc">{desc}</div>'
            f'</div>'
        )

    st.markdown(
        f'<div class="fm-capability-grid">{rows_html}</div>',
        unsafe_allow_html=True
    )


    # ==================================================
    # AI ADVISOR SPOTLIGHT
    # ==================================================

    st.markdown('<div id="ai-advisor"></div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="fm-spotlight">
        <div class="fm-spotlight-eyebrow">Flagship Feature</div>
        <div class="fm-spotlight-title">Meet your AI financial advisor</div>
        <div class="fm-spotlight-text">
            FinMate AI's advisor combines your live financial data with
            AI-driven reasoning to answer questions about budgeting,
            saving and spending — available as soon as you sign in.
        </div>
    </div>
    """, unsafe_allow_html=True)


    # ==================================================
    # FOOTER
    # ==================================================

    st.markdown(
        '<div class="fm-footer">FinMate AI — Personal Finance Platform</div>',
        unsafe_allow_html=True
    )