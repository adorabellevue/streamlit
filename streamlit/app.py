#
#
# This is my first wonderful project.

import streamlit as st
from PIL import Image
import io

st.title("My Website")
myname = st.text_input('Your name')
if myname:
    st.header('your name is ' + myname)
myimg = st.file_uploader("upload a photo", type=['jpg', 'webp'])
if myimg:
    img_data = myimg.read()
    image = Image.open(io.BytesIO(img_data))
    st.image(image, caption='上面是收到的照片', width=300)
