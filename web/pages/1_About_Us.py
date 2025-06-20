import streamlit as st

st.set_page_config(
    page_title="About Us - FinAI Insights",
    page_icon="ℹ️",
    layout="wide"
)

st.title("About FinAI Insights")
st.subheader("Our Mission and Expertise")

st.markdown("""
At **FinAI Insights**, we believe that the future of financial investment lies at the intersection of robust data analysis and advanced Artificial Intelligence.
Our journey began with a vision to democratize sophisticated financial intelligence, making it accessible and understandable for a broader audience.
""")

st.image("[https://placehold.co/800x400/607D8B/FFFFFF?text=Our+Team+Working](https://placehold.co/800x400/607D8B/FFFFFF?text=Our+Team+Working)", caption="Our Dedicated Team")

st.header("Our Mission")
st.markdown("""
Our mission is to empower investors and businesses with precise, AI-driven financial insights that lead to better decision-making,
optimized portfolios, and sustainable growth. We are committed to fostering a deeper understanding of market dynamics
through transparent and reliable analytical solutions.
""")

st.header("Who We Are")
st.markdown("""
FinAI Insights is founded by [Your Name/Founder's Name], a seasoned financial analyst and data scientist with over [X] years
of experience in both traditional finance and cutting-edge AI technologies. Our team comprises experts in machine learning,
quantitative finance, and software engineering, dedicated to pushing the boundaries of what's possible in financial analytics.

We are passionate about leveraging data to uncover opportunities and mitigate risks, providing our clients with a competitive edge.
""")

st.markdown("---")

st.subheader("Our Core Values")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 📈 Innovation")
    st.write("Continuously researching and implementing the latest AI and machine learning techniques.")

with col2:
    st.markdown("### 🤝 Transparency")
    st.write("Providing clear explanations of our methodologies and insights, fostering trust with our clients.")

with col3:
    st.markdown("### 🎯 Client Success")
    st.write("Dedicated to understanding our clients' unique goals and delivering tailored solutions that drive success.")

st.markdown("---")
st.info("Ready to learn more about what we offer? Check out our services!")
st.page_link("pages/2_Our_Services.py", label="View Our Services", icon="➡️")
