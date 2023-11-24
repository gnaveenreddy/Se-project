import streamlit as st
import mysql.connector
import re
from components import login
# Establish connection
if 'signup' not in st.session_state:
    st.session_state.signup = False

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
        trainer=st.selectbox("Select Your Trainer",["Andrew","Tate","Crew","Jenni"])
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
            q="Select user_name from users where user_name= %s"

            cursor.execute(q,(user_name,))
            res=cursor.fetchall()
            if(res):
                st.warning("user already exist")
                login.login_page()
            else:
               query="INSERT INTO users (user_name, user_password,email,age,gender,trainer) VALUES (%s, %s,%s,%s,%s,%s)"
               values = (user_name, password,email,age,gender,trainer)
               cursor.execute(query, values)   
               conn.commit()
               cursor.close()
               conn.close()
               st.session_state.signup=True
               st.success(f"Successfully signed up, {user_name}!")


if __name__ == "__main__":
    signup_form()
