import streamlit as st
import mysql.connector

def authenticate_admin(username, password):
    # Basic admin authentication logic (replace with your actual logic)
    return username == "admin" and password == "admin123"

def admin():
    # Use Streamlit's built-in authentication
    admin_username = st.text_input("Admin Username")
    admin_password = st.text_input("Admin Password", type="password", key="admin_password_key")  # Key is needed for caching

    if st.button("Login as Admin"):
        if authenticate_admin(admin_username, admin_password):
            st.success("Admin authentication successful!")

            conn = mysql.connector.connect(
                host='localhost',
                user='root',
                password='naveen@19',
                database='gym_users'
            )
            cursor = conn.cursor()
            query = "SELECT * FROM users"
            cursor.execute(query)
            result = cursor.fetchall()
            st.write("    **USER DETAILS:**      ")
            if result:
                # Get column names
                columns = [i[0] for i in cursor.description]

                # Display table header  
                st.table([columns] + result)

            else:
                st.warning("No data available.")

            st.write("    **USER REVIEWS:**      ")
            cursor = conn.cursor()
            query = "SELECT * FROM reviews"
            cursor.execute(query)
            result = cursor.fetchall()

            if result:
                # Get column names
                columns = [i[0] for i in cursor.description]

                # Display table header
                st.table([columns] + result)

            else:
                st.warning("No data available.")
        else:
            st.error("Invalid admin credentials. Please try again.")

if __name__ == "__main__":
    admin()
