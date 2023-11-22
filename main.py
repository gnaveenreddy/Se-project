import streamlit as st
from components import home,login,signup,contact_component,subs,secret

st.set_page_config(page_title="Gym Website", page_icon="💪")
# st.title("Welcome to Our Gym!")
nav_selection = st.sidebar.selectbox("Navigation", ["Home", "Login", "Contact Us","SignUP__New user","Join US","Admin"])
if(nav_selection=="Home"):
    home.Home()
elif (nav_selection=="Login"):
    login.login_page()
elif (nav_selection=="SignUP__New user"):
    signup.signup_form()
elif(nav_selection=="Contact Us"):
    contact_component.contact()
elif (nav_selection=="Join US"):
    subs.subs()
elif (nav_selection=="Admin"):
    secret.admin()
    

