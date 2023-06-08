import streamlit as st
import openai


def page_two():
    st.title('OpenAI DALL·E Image Generation')
    st.info("""#### NOTE: you can download image by \
    right clicking on the image and select save image as option""")
    
    with st.form(key="form"):
        prompt = st.text_input(label='Enter text prompt for image generation')
        size = st.selectbox('select size of images', ("256x256", "512x512", "1024x1024"))
        num_images = st.selectbox('Select number of images to be generated', (1,2,3,4))
        submit_button = st.form_submit_button(label='submit') 
    if submit_button:
        if prompt:
            st.text(f"Generating images......")
            response = openai.Image.create(prompt=prompt, n=num_images, size=size)
            
            for idx in range(num_images):
                img_url = response['data'][idx]['url']
                
                st.image(img_url, caption=f"Generated image: {idx+1}", use_column_width=True)