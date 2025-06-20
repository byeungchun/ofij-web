import streamlit as st

st.set_page_config(
    page_title="Our Services - FinAI Insights",
    page_icon="🛠️",
    layout="wide"
)

st.title("Our Services")
st.subheader("Tailored AI-Driven Financial Analysis Solutions")

st.markdown("""
FinAI Insights offers a comprehensive suite of services designed to meet the diverse needs of individual investors,
financial advisors, and corporate clients. Our services harness the power of AI to provide unparalleled depth
and foresight into financial markets.
""")

st.markdown("---")

# Service 1: Portfolio Optimization
st.header("1. AI-Powered Portfolio Optimization")
col1, col2 = st.columns([1, 2])
with col1:
    st.image("https://placehold.co/400x250/8BC34A/FFFFFF?text=Portfolio+Opt", caption="Optimized Portfolios")
with col2:
    st.markdown("""
    Our AI models analyze your current portfolio, risk tolerance, and financial goals to recommend optimal asset allocations.
    We help you achieve maximum returns for a given level of risk, or minimize risk for a desired return.

    **Key Features:**
    * Dynamic asset allocation recommendations
    * Risk assessment and diversification strategies
    * Performance forecasting and scenario analysis
    """)

st.markdown("---")

# Service 2: Market Trend Prediction
st.header("2. Predictive Market Trend Analysis")
col1, col2 = st.columns([1, 2])
with col1:
    st.image("https://placehold.co/400x250/FF9800/FFFFFF?text=Market+Trends", caption="Predicting Market Movements")
with col2:
    st.markdown("""
    Gain an edge with our AI-driven market trend predictions. We analyze vast amounts of historical and real-time data,
    including news sentiment, economic indicators, and technical patterns, to identify emerging trends and potential market shifts.

    **Key Features:**
    * Short-term and long-term market forecasts
    * Sentiment analysis of financial news
    * Identification of undervalued/overvalued assets
    """)

st.markdown("---")

# Service 3: Risk Assessment and Management
st.header("3. Comprehensive Risk Assessment & Management")
col1, col2 = st.columns([1, 2])
with col1:
    st.image("https://placehold.co/400x250/F44336/FFFFFF?text=Risk+Mgmt", caption="Managing Financial Risk")
with col2:
    st.markdown("""
    Understand and manage your financial risks more effectively. Our AI quantifies various types of risks, from market volatility
    to credit risk, and provides strategies to mitigate potential losses, ensuring the resilience of your investments.

    **Key Features:**
    * Value-at-Risk (VaR) and Conditional VaR (CVaR) calculations
    * Stress testing and scenario analysis
    * Early warning systems for potential market downturns
    """)

st.markdown("---")

# Service 4: Custom Financial Analytics Solutions
st.header("4. Custom Financial Analytics Solutions")
col1, col2 = st.columns([1, 2])
with col1:
    st.image("https://placehold.co/400x250/9C27B0/FFFFFF?text=Custom+Solutions", caption="Tailored Solutions")
with col2:
    st.markdown("""
    Do you have unique financial data challenges or specific analytical needs? We offer bespoke AI solutions
    tailored to your precise requirements, from custom model development to integrating our insights into your existing systems.

    **Key Features:**
    * Development of custom AI/ML models
    * Integration with existing financial platforms
    * Consultation and ongoing support
    """)

st.markdown("---")

st.info("Curious about how our AI models work their magic? Learn more about our approach.")
st.page_link("pages/3_Our_Approach.py", label="Discover Our Approach", icon="💡")
