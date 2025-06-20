import streamlit as st

st.set_page_config(
    page_title="Our Approach - FinAI Insights",
    page_icon="💡",
    layout="wide"
)

st.title("Our AI-Driven Approach")
st.subheader("The Science Behind Smarter Financial Decisions")

st.markdown("""
At FinAI Insights, our strength lies in our sophisticated methodology that combines cutting-edge Artificial Intelligence
with deep financial domain expertise. We follow a rigorous process to ensure our insights are not only powerful but also reliable and actionable.
""")

st.markdown("---")

# Step 1: Data Collection & Preparation
st.header("1. Comprehensive Data Collection & Preparation")
col1, col2 = st.columns([1, 2])
with col1:
    st.image("[https://placehold.co/400x250/26A69A/FFFFFF?text=Data+Collection](https://placehold.co/400x250/26A69A/FFFFFF?text=Data+Collection)", caption="Gathering Diverse Data")
with col2:
    st.markdown("""
    We aggregate vast amounts of financial data from diverse sources, ensuring a holistic view of the market.
    This includes:
    * **Market Data:** Historical prices, trading volumes, derivatives, and indices.
    * **Economic Indicators:** Macroeconomic data, inflation rates, employment figures.
    * **News & Sentiment:** Real-time news feeds, social media sentiment, analyst reports.
    * **Company Fundamentals:** Balance sheets, income statements, cash flow.

    Our rigorous data cleaning and preprocessing ensure data quality and consistency, which is crucial for AI model performance.
    """)

st.markdown("---")

# Step 2: Advanced AI Modeling
st.header("2. State-of-the-Art AI Modeling")
col1, col2 = st.columns([1, 2])
with col1:
    st.image("[https://placehold.co/400x250/7E57C2/FFFFFF?text=AI+Modeling](https://placehold.co/400x250/7E57C2/FFFFFF?text=AI+Modeling)", caption="Building Intelligent Models")
with col2:
    st.markdown("""
    We employ a diverse set of advanced AI and machine learning techniques, carefully selected and optimized for financial data.
    Our models include:
    * **Deep Learning Networks:** For pattern recognition in complex, high-dimensional data (e.g., LSTMs for time series).
    * **Reinforcement Learning:** For optimal trading strategies and portfolio management under uncertainty.
    * **Natural Language Processing (NLP):** To extract insights from unstructured text data like news articles and reports.
    * **Ensemble Methods:** Combining multiple models to enhance robustness and predictive accuracy.

    Each model is rigorously tested and validated against historical data to ensure its reliability and performance.
    """)

st.markdown("---")

# Step 3: Insight Generation & Visualization
st.header("3. Actionable Insight Generation & Visualization")
col1, col2 = st.columns([1, 2])
with col1:
    st.image("[https://placehold.co/400x250/FFD54F/333333?text=Insights+Visualization](https://placehold.co/400x250/FFD54F/333333?text=Insights+Visualization)", caption="Clear & Actionable Insights")
with col2:
    st.markdown("""
    The output of our AI models is then translated into clear, concise, and actionable insights.
    We believe that complex analysis should result in simple, understandable recommendations.
    Our visualizations make it easy to grasp complex market dynamics and investment opportunities at a glance.

    **This includes:**
    * Risk scores and heatmaps
    * Predicted price movements and confidence intervals
    * Portfolio diversification metrics
    * Sentiment trends and key drivers
    """)

st.markdown("---")

# Step 4: Continuous Learning & Adaptation
st.header("4. Continuous Learning & Adaptation")
col1, col2 = st.columns([1, 2])
with col1:
    st.image("[https://placehold.co/400x250/EF5350/FFFFFF?text=Continuous+Learning](https://placehold.co/400x250/EF5350/FFFFFF?text=Continuous+Learning)", caption="Adapting to Market Changes")
with col2:
    st.markdown("""
    Financial markets are dynamic. Our AI systems are designed for continuous learning, constantly updating their models
    with new data and adapting to evolving market conditions. This ensures that our insights remain relevant and predictive
    in an ever-changing economic landscape.

    This iterative process allows us to refine our predictions and strategies, providing you with the most current and effective guidance.
    """)

st.markdown("---")

st.info("Ready to take the next step? Get in touch with us!")
st.page_link("pages/4_Contact_Us.py", label="Contact Us Now", icon="✉️")
