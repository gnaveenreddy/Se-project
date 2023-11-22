import streamlit as st
import mysql.connector
import re

# Establish connection
def signup_form():
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='naveen@19',
        database='gym_users'
)
    cursor=conn.cursor()
    st.header("Sign Up")

    # Create a form for user signup
    with st.form("signup_form"):
        # Add form elements
        user_name = st.text_input("Enter Your Name")
        gender = st.radio("Select your gender", ["Male", "Female", "Other"])
        email=st.text_input("Enter your Email")
        password = st.text_input("Enter Your Password", type="password")
        confirm_password = st.text_input("Confirm Password", type="password")
        age = st.slider("Select your age", min_value=0, max_value=100, value=25)
        agree_terms = st.checkbox("I agree to the terms and conditions")
        submit_button = st.form_submit_button("Sign Up")

    regex_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    # Handle form submission
    if submit_button:
        # Basic form validation
        if not user_name or not password or not confirm_password:
            st.warning("No feild cannot be empty")
        elif not (re.match(regex_pattern, email)):
            st.warning("Invalid  email address Please enter the valid one!")
        elif password != confirm_password:
            st.warning("Password and confirm password do not match.")
        else:
            # Add your signup logic here (e.g., store user data in a database)
            query="INSERT INTO users (user_name, user_password,email,age,gender) VALUES (%s, %s,%s,%s,%s)"
            values = (user_name, password,email,age,gender)
            cursor.execute(query, values)   
            conn.commit()
            cursor.close()
            conn.close()
            st.success(f"Successfully signed up, {user_name}!")


if __name__ == "__main__":
    signup_form()
