# components/payment.py

import streamlit as st

def payment(amount):
    st.title("Payment Page")

    # Display the selected subscription type and amount
    st.write(f"Selected Subscription Type: {'Premium' if amount == 20000 else 'Basic'}")
    st.write(f"Amount to Pay: ₹{amount}/-")

    # Collect payment details
    card_number = st.text_input("Card Number")
    exp_month = st.number_input("Expiry Month", min_value=1, max_value=12)
    exp_year = st.number_input("Expiry Year", min_value=2022, max_value=2030)
    cvc = st.text_input("CVC",type="password")

    # Process payment when a button is clicked
    if st.button("Process Payment"):
        if(card_number and exp_month and exp_year and  cvc):
            st.success("Payment is succesfull")
        else:
            st.warning("Payment not successfull! Try again")

