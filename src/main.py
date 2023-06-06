import streamlit as st
import openai
import os
from dotenv import load_dotenv
from src.page_1 import page_one
from src.page_2 import page_two
from src.page_3 import  page_three

load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')


pages = {
    "Introduction": page_one,
    "Text to image": page_two,
    "Image variation": page_three,
    # "Image edit": page4
}


page = st.sidebar.selectbox('select page', list(pages.keys()))

pages[page]()