import streamlit as st
import mysql.connector

if 'selected_user_id' not in st.session_state:
    st.session_state.selected_user_id = None

# Check if 'reviews' is already in session_state
if 'reviews' not in st.session_state:
    st.session_state.reviews = {"user_id": None, "rating": 0, "comment": ""}

# Function to fetch user IDs from the database
def fetch_user_ids():
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='naveen@19',
        database='gym_users'
    )
    cursor = connection.cursor()
    query = "SELECT user_id FROM users"
    cursor.execute(query)
    user_ids = [row[0] for row in cursor.fetchall()]
    cursor.close()
    connection.close()
    return user_ids

def review():
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='naveen@19',
        database='gym_users'
    )
    cursor = conn.cursor()

    user_ids = fetch_user_ids()

    # Create a dropdown to select a user ID
    selected_user_id = st.selectbox("Select User ID:", user_ids)

    q = f"SELECT trainer FROM users WHERE user_id={selected_user_id}"
    cursor.execute(q)
    t = cursor.fetchone()

    # Optionally, you can display the selected user ID
    if selected_user_id:
        st.write(f"Selected User ID: {selected_user_id}")
        st.session_state.selected_user_id = selected_user_id
    else:
        st.warning("Please select a user ID.")

    # Section for reviews
    st.header("Give Reviews")

    # Create a form for reviews
    review_rating = st.slider("Rate the user (1-5):", min_value=1, max_value=5, value=st.session_state.reviews["rating"])
    review_comment = st.text_area("Leave a comment:", st.session_state.reviews["comment"])

    if st.button("Submit Review"):
        if st.session_state.selected_user_id:
            # Update the 'reviews' in session_state
            st.session_state.reviews = {"user_id": st.session_state.selected_user_id, "rating": review_rating, "comment": review_comment}

            # Replace 'reviews' with your table name
            cursor.execute("INSERT INTO reviews (user_id, trainer, rating, comment) VALUES (%s, %s, %s, %s)",
                           (st.session_state.selected_user_id, t[0], review_rating, review_comment))

            conn.commit()

            st.success("Review submitted successfully!")
        else:
            st.warning("Please select a user ID before submitting a review.")

    # Display the reviews
    # You can add a section to display the reviews if needed

    # Close the cursor and connection
    cursor.close()
    conn.close()

