import streamlit as st
from components import home,login,signup,contact_component,subs,secret,reveiws
# if "login" not in st.session_state:
#     st.session_state.login=False

# st.set_page_config(page_title="Gym Website", page_icon="💪")
# st.title("Welcome to Our Power Pulse GYM!")
# st.image("https://cdn.dribbble.com/users/3437915/screenshots/15106661/media/15ff29d5f73ad8d8068dd1150267d57e.jpg?resize=400x300&vertical=center",use_column_width=True)
# signup.signup_form()
import streamlit as st
st.set_page_config(layout="wide",page_title="Gym Website", page_icon="💪")
# Custom HTML/CSS for the banner
custom_html = """
<div class="banner">
    <img src="https://img.freepik.com/premium-photo/wide-banner-with-many-random-square-hexagons-charcoal-dark-black-color_105589-1820.jpg" alt="Banner Image">
</div>
<style>
    .banner {
        width: 160%;
        height: 200px;
        overflow: hidden;
        flex:auto;
    }
    .banner img {
        width: 100%;
        object-fit: cover;
    }
</style>
"""
# Display the custom HTML
st.components.v1.html(custom_html)

# Main content
st.title("Welcome Muscle Crafters GYM")
st.header("Our Facilities")
st.markdown(
    """
    Welcome to our **gym**! We are passionate about fitness and dedicated to helping you achieve your health goals."""
)
image_paths = [
    "https://images.pexels.com/photos/7174396/pexels-photo-7174396.jpeg?auto=compress&cs=tinysrgb&w=600",
    "https://img.freepik.com/free-photo/gym-with-treadmills-light-wall_1340-37799.jpg",
    "https://t4.ftcdn.net/jpg/04/87/53/03/240_F_487530379_yetg9Zqrltr27ktNm8Qe2WJ5DHFciUhm.jpg",
    "https://t4.ftcdn.net/jpg/06/10/63/21/240_F_610632116_VhHJygoD5cFAdhp2arETpTa8fWkXx2tw.jpg"
    
    # Add more image paths here
]
# Create columns to display images horizontallif
col1, col2,col3,col4 = st.columns(4)  # Adjust the number of columns as needed
    
for i, image_path in enumerate(image_paths):
            
            if i % 4 == 0:
                col1.image(image_path,caption="Workout Area", use_column_width=True)
            elif i % 4 == 1:
                col2.image(image_path, caption="Thread Mill Zone",use_column_width=True)
            elif i % 4 == 2:
                col3.image(image_path, caption="Hard Workout Zone",use_column_width=True)
            elif i % 4 == 3:
                col4.image(image_path, caption="Peace Zone",use_column_width=True)

st.header("Our Trainers")
st.write("We are a dedicated team of fitness professionals committed to helping you achieve your goals.")
st.write("Our Trainers are our assets and good guide for your overall fitness.")
image_paths = [
    "https://images.pexels.com/photos/6455821/pexels-photo-6455821.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2",
    "https://images.pexels.com/photos/6551061/pexels-photo-6551061.jpeg?auto=compress&cs=tinysrgb&w=600",
    "https://images.pexels.com/photos/7991689/pexels-photo-7991689.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2",
    "https://images.pexels.com/photos/4498220/pexels-photo-4498220.jpeg?auto=compress&cs=tinysrgb&w=600"
    
    # Add more image paths here
]
# Create columns to display images horizontall
col1, col2,col3,col4 = st.columns(4)  # Adjust the number of columns as needed
    
for i, image_path in enumerate(image_paths):
            
            if i % 4 == 0:
                col1.image(image_path,caption="Andrew (Personal Trainer", use_column_width=True)
            elif i % 4 == 1:
                col2.image(image_path, caption="Tate (Aerobic Trainer)",use_column_width=True)
            elif i % 4 == 2:
                col3.image(image_path, caption="Crew (Fitness Director)",use_column_width=True)
            elif i % 4 == 3:
                col4.image(image_path, caption="Jenni (Yoga Trainer)",use_column_width=True)


# s.write("Welcome to my Streamlit app!")
# s.write("This is the main content area.")
# if st.button("Signup"):
#      signup.signup_form()
# if st.button("Login"):
#      login.login_page()
nav_selection = st.sidebar.selectbox("Navigation", ["Home", "Login", "Contact Us","SignUP__New user","Join US","Admin","Feedback"])
if(nav_selection=="Home"):
       if st.session_state.login or st.session_state.signup:
         home.Home()
elif (nav_selection=="Login"):
    login.login_page()
elif (nav_selection=="SignUP__New user"):
    signup.signup_form()
elif(nav_selection=="Contact Us"):
    if st.session_state.login or st.session_state.signup:
       contact_component.contact()
elif (nav_selection=="Join US"):
    if st.session_state.login or st.session_state.signup:
       subs.subs()
elif (nav_selection=="Admin"):
    secret.admin()
elif (nav_selection=="Feedback"):
    if st.session_state.login or st.session_state.signup:
        reveiws.review()
      
    

