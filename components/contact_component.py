# components/about_component.py
def contact():
      
    import PIL as Image
    import streamlit as st
    
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
    
    
    # st.header("About Us")
    st.header("Contact Us")
    st.write("Feel free to reach out to us using the contact information below.")
    # Add Instagram and Facebook logos
    st.image("https://w7.pngwing.com/pngs/722/1011/png-transparent-logo-icon-instagram-logo-instagram-logo-purple-violet-text-thumbnail.png", width=50)
    st.image("data:image/png;base64,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", width=50)
    # Display contact information
    st.markdown("**Email:** fitness@gym.com")
    st.markdown("**Phone:** +1 (123) 456-7890")
    st.markdown("**Address:** New york city, Church Street")
    # image = Image.open('Cardio_2.jpg')
    # st.image('./Cardio_2.jpg', caption='Sunrise by the mountains')
    # Ad custom styling
    st.markdown(
        """
        <style>
            .main {
                color: orange;
                font-size: 25px;
            }
            .sidebar .sidebar-content {
                background-color: #f0f0f0;
            }
        </style>
        """,
        unsafe_allow_html=True
    )
if __name__ == "__main__":
    contact()