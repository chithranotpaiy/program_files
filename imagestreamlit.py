import streamlit as st
from PIL import Image


def main():
    st.title("Display Image Example")


    image = Image.open("solve.jpg")

    st.image(image, caption='Sunset in the mountains', use_column_width=200)



main()
