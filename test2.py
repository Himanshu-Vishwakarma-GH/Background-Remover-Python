from rembg import remove
import streamlit as st
from PIL import Image
import io

st.title("Free Background Remover")
st.write("#### Upload an image to remove the background")

input = st.file_uploader(" ")

if input is not None:
    see = Image.open(input)
    edit = remove(see)  # 'see' ko pass karein 'input' ki jagah

    # Image ko bytes mein convert karna
    buf = io.BytesIO()
    edit.save(buf, format='PNG')
    byte_im = buf.getvalue()

    if st.button("Convert"):

        st.image(see, caption='Original Image')
        st.image(edit, caption='Edited Image')  # Image ko display karein

        st.download_button("Download Image",byte_im, file_name="edited_image.png")  
        # Download button ke liye correct parameters
