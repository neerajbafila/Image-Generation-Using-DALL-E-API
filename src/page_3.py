import streamlit as st
from src.utils.utils import resize_image, get_width_height
from PIL import Image
import openai

def page_three():
    st.title("OpenAI DALL·E Image Variation")
    st.info("""#### NOTE: you can download image by \
    right clicking on the image and select save image as option""")
    
    with st.form(key="form"):
        uploaded_file = st.file_uploader(label='upload file', type=['png', 'jpeg'])
        size = st.selectbox('select size of image', ('256x256', '512x512', '1024x1024'))
        num_images = st.selectbox('enter the number of images to be generated', (1,2,3,4))

        submit = st.form_submit_button(label='submit')
    if submit:
        image = Image.open(uploaded_file)
        st.image(image, caption="uploaded image", use_column_width=True)
        width, height =  get_width_height(size)
        resize_img =  resize_image(image, width, height)
        st.text('Generating images with variation....')
        response = openai.Image.create_variation(image=resize_img, n=num_images, size=size)

        for idx in range(num_images):
            img_url = response['data'][idx]['url']

            st.image(img_url, caption=f'generated image {idx+1}', use_column_width=True)
            



