import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image
st.set_page_config(page_title="My Webpage",page_icon=":tada:",layout="wide")

def load_lottieurl(url):
    r=requests.get(url)
    if r.status_code!=200:
        return None
    return r.json()

#--------Load Assets------------
lottie_coding=load_lottieurl("https://lottie.host/d4550382-f326-4e9f-bf23-18385d9ac61e/Xqw0YnEtJ8.json")
img_1=Image.open("images/project img1.png")
img_2=Image.open("images/project img21.jpg")
img_3=Image.open("images/project img3.png")
#-------Header Section----------
with st.container():
    left,right=st.columns((1,2))
    with right:
        st.subheader("Hi,I'm Rakshitha Kini :wave:")
        st.title("Welcome is My Web Page")
        st.write("Currently pursuing B.E in Information Science")
        st.write("My [LinkedIn >](https://www.linkedin.com/in/rakshitha-kini-2a3ab7205)")
    with left:
        st.image(img_2,width=250)

#--------What I Do--------
with st.container():
    st.write("-----")
    left_column,right_column=st.columns(2)
    with left_column:
        st.header("About Me")
        st.write("##")
        st.write(
            """ 
            -I'm Passionate about learning new concepts practically
            - I come from a rural area and hence the computers and Technology have always fascinated me.
            - Currently working on improving myself both on profesional and personal levels.
            - Apart from Programming and Technology ,I'm also fascinated by Astronomy and Human Psychology.
            - My Hobbies include Creative Writing and Reading Books.
            """
        )
    with right_column:
        st_lottie(lottie_coding,height=300,key="coding")

#-----My Projects-------
with st.container():
    st.write("-------")
    img_column,text_column=st.columns((1,2))
    with img_column:
        st.image(img_1)
        st.write("##")
        st.write("##")
        st.image(img_3)
    with text_column:
        st.subheader("Academic Projects")
        st.write("##")
        st.write(" 1. Shrimp Culture Management")
        st.write("""
                   - This project aims to develop an application that helps shrimp farmers to manage their cultivativation ponds.
                     It uses Java for front-end and mySQL to perform CRUD operations on the database. 
                     Along with CRUD, various other opertions like Event Scheduling is also performed.
                   - Front end was developed in Apache NetBeans IDE using swings and backend was developed using MySQL workbench.
                 """)
        st.write("##")
        st.write(" 2. FIR Management System using File Structures")
        st.write("""
                    - It is an application designed to streamline the process of registering,managing,an accessing FIRs for law enforcement agencies.
                    - It was developed as a part of File Structure Mini Project to demonstrate CRUD operations on a file systems.
                    - It implements SHA-256 for password hashing.
                    - The application is developed using Python.
                """)
        st.write("##")
        st.write("##")
        st.subheader("Non-Academic Projects")
        st.write("##")
        st.write(" 1. WallMart Data Analysis")
        st.write("""
                    - It is a Full Stack Project which classifies the visitors visiting the wallmart based on their age and gender.
                    - It uses HTML,CSS , Bootstrap and JavaScript to design and develop the web application.

                 """)
                 