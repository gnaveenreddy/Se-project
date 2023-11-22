import streamlit as st
import streamlit as st
import mysql.connector
from components import signup
def login_page():
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='naveen@19',
        database='gym_users'
)
    cursor=conn.cursor()
    st.image("https://thumbs.dreamstime.com/b/sport-gym-interior-workout-equipment-copy-space-flat-vector-illustration-86243138.jpg?w=1400", use_column_width=True)
    st.title("Login Page")
    

    # Create a form for user login
    with st.form("login_form"):
        # Add form elements
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submit_button = st.form_submit_button("Login")
        

    # Handle form submission
    if submit_button:
        # Basic login validation (replace with your actual authentication logic)
        query="SELECT u.user_password FROM users u WHERE u.user_name = %s"
        cursor.execute(query, (username,))
        result = cursor.fetchone()
        if(result):
           
           fetched_password=result[0]
           if  password == fetched_password:
               st.success(f"Welcome, {username}!")
            # Add logic for redirecting to the user's dashboard or another page
           else:

            st.error("Invalid username or password. Please try again.")
        else:
           st.warning("You are a new user lets go to Sigup page")
           signup.signup_form()
           

if __name__ == "__main__":
    login_page()
