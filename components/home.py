import streamlit as st
from components import classes_component
def Home():
        
    # st.header("Welcome to our gym! Get fit and stay healthy.")
        
    # st.title("Welcome to Our Gym!")
    st.image("https://t3.ftcdn.net/jpg/03/19/27/58/360_F_319275875_vqeGDiMVZZrBd9m8B8xhoK0uqCawjbPU.jpg", caption="Gym Banner", use_column_width=True)
    st.write(
        "At our gym, we are dedicated to helping you achieve your fitness goals. "
        "Explore our state-of-the-art facilities, meet our experienced trainers, "
        "and discover a range of fitness classes tailored to your needs."
    )
            # user_name = st.text_input("Enter Your Name:")
    st.header("Get Started To EXPLORE")
    selected_class = st.selectbox("Select a Fitness Class:", ["Cardio", "Weightlifting", "Yoga"])
    st.session_state.login_form=True
    if selected_class=="Cardio":
           classes_component.Cardio()
    if selected_class=="Yoga":
           classes_component.Yoga()
    if selected_class=="Weightlifting":
           classes_component.Weight()
    # Add interactive elements
    
    
if __name__ == "__main__":
    Home()    