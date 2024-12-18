#
# change line locally
#
# This is my first wonderful project.

import streamlit as st
from PIL import Image
import io

st.set_page_config(page_title="Streamlit Sidebar Example", layout="wide")

st.title("My Website")

face, photo_read, tts = st.tabs(["Face recognition", "Read photo", "Text-to-speech"])

with face:
    myname = st.text_input('Your name')
    if myname:
        st.header('your name is ' + myname)
    myimg = st.file_uploader("upload a photo", type=['jpg', 'webp'])
    if myimg:
        img_data = myimg.read()
        image = Image.open(io.BytesIO(img_data))
        st.image(image, caption='上面是收到的照片', width=300)

with photo_read:
    st.write("photo read")

with tts:
    st.write("text-to-speech")