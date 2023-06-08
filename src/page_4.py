import streamlit as st
from PIL import Image
import openai
from rembg import remove
from src.utils.utils import resize_image, get_width_height


def page_four():
    st.title("OpenAI DALL·E Image Editing")
    st.info("""#### NOTE: you can download image by \
    right clicking on the image and select save image as option""")

    with st.form(key='form'):
        uploaded_file = st.file_uploader(label="Choose an image file to be edited", type=['png', 'jpg'])
        mask_file = st.file_uploader(label="chose the mask file", type=['png', 'jpg'])
        prompt = st.text_input("enter a text prompt")
        size = st.selectbox('Select size of the images', ('256x256', '512x512', '1024x1024'))
        num_images = st.selectbox('enter number of images to be generated',(1,2,3,4))
        submit_button = st.form_submit_button(label='submit')
    
    if submit_button:
        if (uploaded_file is not None) and (mask_file is not None) and prompt:
            our_img = Image.open(uploaded_file)
            mask_img = Image.open(mask_file)
            width, height = get_width_height(size)
            our_img = resize_image(our_img, width, height)
            mask_img = resize_image(mask_img, width, height)

            st.image(our_img, "Uploaded image", use_column_width=True)
            st.image(mask_img, "Mask image", use_column_width=True)
            backround_removed_mask = remove(mask_img)
            # st.image(backround_removed_mask, "back", use_column_width=True)
            st.text('Generating images....')
            response = openai.Image.create_edit(image=our_img, mask=backround_removed_mask, prompt=prompt, n=num_images,
                                                size=size)
            
            for idx in range(num_images):
                img_url = response['data'][idx]['url']

                st.image(img_url, caption=f'Generated image : {idx+1}', use_column_width=True)



                                         
                                         