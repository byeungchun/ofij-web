import streamlit as st
import requests # Used for sending form data to an external service

st.set_page_config(
    page_title="Contact Us - FinAI Insights",
    page_icon="✉️",
    layout="wide"
)

st.title("Contact Us")
st.subheader("Get in Touch for Your Financial Analysis Needs")

st.markdown("""
We're here to help you unlock the power of AI for your financial investments.
Whether you have questions about our services, need a custom solution, or just want to discuss how AI can benefit you,
feel free to reach out.
""")

st.markdown("---")

st.header("Send Us a Message")

# Simple contact form using Streamlit inputs
with st.form("contact_form"):
    name = st.text_input("Your Name", placeholder="John Doe")
    email = st.text_input("Your Email", placeholder="john.doe@example.com")
    subject = st.text_input("Subject", placeholder="Inquiry about Portfolio Optimization")
    message = st.text_area("Your Message", placeholder="I'm interested in learning more about your AI-driven financial analysis services...")

    # Every form must have a submit button.
    submitted = st.form_submit_button("Send Message")

    if submitted:
        if name and email and subject and message:
            # Here you would typically integrate with an email service (e.g., SendGrid, Mailgun)
            # or a form backend (e.g., Google Forms, Formspree, custom API endpoint)
            # For demonstration, we'll just show a success message.
            st.success("Thank you for your message! We will get back to you shortly.")

            # Example of how you might send data to an external service (conceptual)
            # This requires a backend to receive the data and handle email sending.
            # form_data = {
            #     "name": name,
            #     "email": email,
            #     "subject": subject,
            #     "message": message
            # }
            # try:
            #     # Replace with your actual backend endpoint
            #     response = requests.post("YOUR_FORM_SUBMISSION_ENDPOINT", json=form_data)
            #     if response.status_code == 200:
            #         st.success("Thank you for your message! We will get back to you shortly.")
            #     else:
            #         st.error("There was an error sending your message. Please try again or contact us directly.")
            # except Exception as e:
            #     st.error(f"An error occurred: {e}. Please try again.")

        else:
            st.error("Please fill in all fields.")

st.markdown("---")

st.header("Other Ways to Connect")
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 📍 Location")
    st.write("FinAI Insights HQ")
    st.write("[Your Business Address Here]")
    st.write("City, Country, Zip Code")

with col2:
    st.markdown("### 📞 Phone & Email")
    st.write("Phone: [+1 234 567 8900](tel:+12345678900)")
    st.write("Email: [info@finaiinsights.com](mailto:info@finaiinsights.com)")
    st.write("Business Hours: Mon-Fri, 9:00 AM - 5:00 PM [Your Timezone]")

st.markdown("---")

st.markdown("We look forward to hearing from you!")

