import streamlit as st

# Configure the page settings
st.set_page_config(
    page_title="FinAI Insights - AI-Driven Financial Analysis",
    page_icon="💰", # A finance-related emoji icon
    layout="wide", # Use wide layout for better content display
    initial_sidebar_state="expanded" # Keep sidebar expanded by default
)

# --- Header Section ---
st.image("https://placehold.co/1200x250/336699/FFFFFF?text=FinAI+Insights+-+AI+Driven+Financial+Analysis", use_column_width=True)
st.title("Welcome to FinAI Insights")
st.subheader("Leveraging AI for Smarter Financial Decisions")

# --- Introduction ---
st.markdown("""
Welcome to **FinAI Insights**, your partner in navigating the complex world of financial markets with cutting-edge Artificial Intelligence.
We transform raw financial data into actionable insights, helping investors, businesses, and individuals make informed decisions and optimize their strategies.

Our proprietary AI models analyze vast datasets, identify hidden patterns, and forecast market trends with a level of precision
that traditional methods simply cannot match. Whether you're looking to enhance your portfolio performance, mitigate risks,
or understand market dynamics, FinAI Insights provides the clarity you need.
""")

st.markdown("---") # Horizontal line separator

# --- Key Value Proposition Section ---
st.header("Why Choose FinAI Insights?")
col1, col2, col3 = st.columns(3) # Create three columns for features

with col1:
    st.subheader("🧠 AI-Powered Accuracy")
    st.write("""
    Our advanced machine learning algorithms continuously learn and adapt to market shifts,
    providing highly accurate predictions and deep analytical insights.
    """)
    st.image("https://placehold.co/300x200/4CAF50/FFFFFF?text=AI+Accuracy", caption="AI-Powered Insights")

with col2:
    st.subheader("💡 Actionable Intelligence")
    st.write("""
    We don't just provide data; we provide clear, actionable recommendations
    tailored to your specific financial goals and risk tolerance.
    """)
    st.image("https://placehold.co/300x200/FFC107/FFFFFF?text=Actionable+Insights", caption="Actionable Intelligence")


with col3:
    st.subheader("🔒 Secure & Confidential")
    st.write("""
    Your financial data and investment strategies are handled with the utmost
    confidentiality and secured using industry-leading protocols.
    """)
    st.image("https://placehold.co/300x200/2196F3/FFFFFF?text=Secure+Data", caption="Secure & Confidential")

st.markdown("---")

# --- Call to Action ---
st.header("Ready to Transform Your Financial Strategy?")
st.markdown("""
Explore our services to see how we can help you achieve your financial objectives.
""")
# Use st.page_link for navigation to specific pages
st.page_link("pages/2_Our_Services.py", label="Explore Our Services", icon="➡️")

st.markdown("---")

# --- Footer ---
st.markdown("© 2025 FinAI Insights. All rights reserved.")
st.markdown("Disclaimer: Financial investment involves risk. Our analysis provides insights and should not be considered financial advice.")
