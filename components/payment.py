# components/payment.py

import streamlit as st
import stripe

def payment(amount):
    


# Set your Stripe API keys
    stripe.api_key = 'your_secret_key'
    
    st.title("Simple Payment Page")
    
    # Payment form
    st.header("Payment Details")
    name = st.text_input("Full Name")
    email = st.text_input("Email")
    card_number = st.text_input("Card Number")
    exp_date = st.text_input("Expiry Date (MM/YY)")
    cvc = st.text_input("CVC")
    
    # Payment button
    if st.button("Make Payment"):
        # Create a payment intent with the Stripe API
        try:
            intent = stripe.PaymentIntent.create(
                amount=1000,  # Amount in cents
                currency="usd",
                description="Streamlit Payment Example",
            )
            st.success(f"Payment Successful! Payment ID: {intent.id}")
        except stripe.error.CardError as e:
            st.error(f"Payment failed. Error: {e.error.message}")
    
    
    
    