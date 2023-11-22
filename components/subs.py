import streamlit as st
from components import payment

def subs():
    st.title("Gym Subscription Banners")


    st.markdown(
        """
        <div style="display:flex;justify-content:space-around;background-color:#4CAF50;padding:20px;color:white;text-align:center;">
            <div>
                <h2>Basic Subscription</h2>
                <p>Access to essential fitness content and standard training plans.</p>
                <p>Price: ₹9,000/-</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.write("\n")
    basic_button_clicked = st.button("Subscribe to Basic Subscription")
    if basic_button_clicked:
        payment.payment(9000)

    # Premium Subscription Banner


    st.markdown(
        """
        <div style="display:flex;justify-content:space-around;background-color:#FFD700;padding:20px;color:black;text-align:center;">
            <div>
                <h2>Premium Subscription</h2>
                <p>Unlock premium fitness content, personalized training plans, and exclusive benefits.</p>
                <p>Price: ₹20,000/-</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.write("\n")
    premium_button_clicked = st.button("Subscribe to Premium Subscription")
    if premium_button_clicked:
        payment.payment(20000)

if __name__ == "__main__":
    subs()
