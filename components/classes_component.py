import streamlit as st

def Cardio():
    st.session_state.login=True
    st.header("Cardio Section")
    st.write("Explore our variety of fitness classes to find the perfect workout for you.")
    
    image_paths = [
            "https://gymvisual.com/img/p/2/2/9/8/8/22988.gif",
            "https://gymvisual.com/img/p/1/5/9/8/4/15984.gif",
            "https://gymvisual.com/img/p/1/5/9/9/4/15994.gif",
            "https://gymvisual.com/img/p/1/5/9/8/5/15985.gif"
            
            # Add more image paths here
        ]
    
        # Create columns to display images horizontally
    col1, col2,col3,col4 = st.columns(4)  # Adjust the number of columns as needed
    
    for i, image_path in enumerate(image_paths):
            
            if i % 4 == 0:
                col1.image(image_path,caption="Double Jump Rope", use_column_width=True)
            elif i % 4 == 1:
                col2.image(image_path, caption="High Knee Skips",use_column_width=True)
            elif i % 4 == 2:
                col3.image(image_path, caption="Skater Hops",use_column_width=True)
            elif i % 4 == 3:
                col4.image(image_path, caption="Jumping Jack",use_column_width=True)
    image_paths1 = [
            "https://gymvisual.com/img/p/1/5/8/7/2/15872.gif",
            "https://gymvisual.com/img/p/1/5/5/7/8/15578.gif",
            "https://gymvisual.com/img/p/2/5/0/2/5/25025.gif",
            "https://gymvisual.com/img/p/1/5/8/3/9/15839.gif"
            
            # Add more image paths here
        ]

    col1, col2,col3,col4 = st.columns(4)  # Adjust the number of columns as needed
    
    for i, image_path in enumerate(image_paths1):
            
            if i % 4 == 0:
                col1.image(image_path,caption="Cycle Cross Training", use_column_width=True)
            elif i % 4 == 1:
                col2.image(image_path, caption="Rowing ",use_column_width=True)
            elif i % 4 == 2:
                col3.image(image_path, caption="Run (equipment )",use_column_width=True)
            elif i % 4 == 3:
                col4.image(image_path, caption="Hands Bike",use_column_width=True)
    

    video_file = open('P:/Se project/images/production_id_4367572 (1080p).mp4', 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes)
    
    # st.image("https://i.gifer.com/K8bI.gif", caption="Push_ups",)
    # st.image("https://i.gifer.com/7q2s.gif", caption="Push_ups")
if __name__ == "__main__":
    Cardio()

def Yoga():
    st.session_state.login=True
    st.header("Yoga Section")
    st.write("Explore our variety of Yoga classes for you.")
    
    image_paths = [
            "https://gymvisual.com/6497-catalog_default/full-lotus-yoga-pose.jpg",
            "https://gymvisual.com/img/p/2/2/9/3/8/22938.gif",
            "https://gymvisual.com/img/p/2/8/5/7/5/28575.gif",
            "https://gymvisual.com/img/p/2/7/4/6/2/27462.gif"
            
            # Add more image paths here
        ]
    
        # Create columns to display images horizontally
    col1, col2,col3,col4 = st.columns(4)  # Adjust the number of columns as needed
    
    for i, image_path in enumerate(image_paths):
            
            if i % 4 == 0:
                col1.image(image_path,caption="Full lotus yoga pose", use_column_width=True)
            elif i % 4 == 1:
                col2.image(image_path, caption="Butterfly Yoga Flaps",use_column_width=True)
            elif i % 4 == 2:
                col3.image(image_path, caption="Yoga Vjrasana ",use_column_width=True)
            elif i % 4 == 3:
                col4.image(image_path, caption="Tiger Yoga pose",use_column_width=True)


    image_paths1 = [
            "https://gymvisual.com/img/p/2/7/2/4/9/27249.gif",
            "https://gymvisual.com/img/p/2/7/2/3/8/27238.gif",
            "https://gymvisual.com/img/p/2/7/2/5/1/27251.gif",
            "https://gymvisual.com/6505-catalog_default/shoulder-stand-yoga-pose.jpg"
            
            # Add more image paths here
        ]
    
        # Create columns to display images horizontally
    col1, col2,col3,col4 = st.columns(4)  # Adjust the number of columns as needed
    
    for i, image_path in enumerate(image_paths1):
            
            if i % 4 == 0:
                col1.image(image_path,caption="Ardha Matsyendrasana", use_column_width=True)
            elif i % 4 == 1:
                col2.image(image_path, caption="Cobra Yoga POs",use_column_width=True)
            elif i % 4 == 2:
                col3.image(image_path, caption="Pavanamuktasana Yoga ",use_column_width=True)
            elif i % 4 == 3:
                col4.image(image_path, caption="shoulder-stand-yoga-pose",use_column_width=True)
    
    video_file = open('P:/Se project/images/1064549986-preview.mp4', 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes)

    #Video from URL (e.g., YouTube)
    # st.subheader("Video from URL")
    # st.video("https://www.shutterstock.com/video/clip-1064549986-lifestyle-portrait-calm-relaxed-beautiful-multiethnic-diverse")
    
    
    # st.image("https://i.gifer.com/K8bI.gif", caption="Push_ups",)
    # st.image("https://i.gifer.com/7q2s.gif", caption="Push_ups")


if __name__ == "__main__":
    Yoga()

def Weight():
    st.session_state.login=True
    st.header("Weight-Lifting  Section")
    st.write("Explore our variety of Weight-Lifting practices and Competitions for you.")
    
    image_paths1 = [
            "https://gymvisual.com/img/p/1/5/8/8/0/15880.gif",
            "https://gymvisual.com/img/p/1/5/8/8/6/15886.gif",
            "https://gymvisual.com/img/p/1/5/8/7/5/15875.gif",
            "https://gymvisual.com/img/p/1/5/8/8/7/15887.gif"
            
            # Add more image paths here
        ]
    
        # Create columns to display images horizontally
    col1, col2,col3,col4 = st.columns(4)  # Adjust the number of columns as needed
    
    for i, image_path in enumerate(image_paths1):
            
            if i % 4 == 0:
                col1.image(image_path,caption="Bending Lift", use_column_width=True)
            elif i % 4 == 1:
                col2.image(image_path, caption="Stand lift",use_column_width=True)
            elif i % 4 == 2:
                col3.image(image_path, caption="Slept lift",use_column_width=True)
            elif i % 4 == 3:
                col4.image(image_path, caption="sit lift",use_column_width=True)
    image_paths = [
         "https://gymvisual.com/img/p/2/6/5/0/3/26503.gif",
            "https://gymvisual.com/img/p/1/5/5/3/0/15530.gif",
            "https://gymvisual.com/img/p/1/5/8/9/0/15890.gif",
            "https://gymvisual.com/img/p/1/5/9/5/6/15956.gif"
            
            # Add more image paths here
        ]
    
        # Create columns to display images horizontally
    col1, col2,col3,col4 = st.columns(4)  # Adjust the number of columns as needed
    
    for i, image_path in enumerate(image_paths):
            
            if i % 4 == 0:
                col1.image(image_path,caption="Barbel Deadlift from Blocks", use_column_width=True)
            elif i % 4 == 1:
                col2.image(image_path, caption="Barbell Hip Thrust",use_column_width=True)
            elif i % 4 == 2:
                col3.image(image_path, caption="Barbell Squat",use_column_width=True)
            elif i % 4 == 3:
                col4.image(image_path, caption="Strong Man front Chest",use_column_width=True)
    
   

    #Video from URL (e.g., YouTube)
    # st.subheader("Video from URL")
    # st.video("https://www.shutterstock.com/video/clip-1064549986-lifestyle-portrait-calm-relaxed-beautiful-multiethnic-diverse")
    
    
    # st.image("https://i.gifer.com/K8bI.gif", caption="Push_ups",)
    # st.image("https://i.gifer.com/7q2s.gif", caption="Push_ups")
if __name__ == "__main__":
    Weight()


     