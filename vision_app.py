from dotenv import load_dotenv
load_dotenv()

from PIL import Image
import streamlit as st
import os
import google.generativeai as genai


api_key = st.secrets['API_KEY']

# genai.configure(api_key = os.getenv('API_KEY'))
genai.configure(api_key = api_key)

model = genai.GenerativeModel("gemini-1.5-pro")

def get_reponse(input,image):
    if input != '':
        response = model.generate_content([input,image])
    else:
        response = model.generate_content(image)
    return response.text

st.set_page_config(page_title="Gemini Vision App", page_icon=":smile:",layout="wide")

st.header("Google Gemini Image")

input = st.text_input("Input : ", key = "input")

uploaded_image = st.file_uploader("Upload Your Query Image", type = ['jpg', 'png', 'jpeg'])

image = ""
if uploaded_image is not None:
    image = Image.open(uploaded_image)
    st.image(image, caption = "Your Uploaded Image.", use_column_width = True)

submit = st.button("Submit")

if submit:
    response = get_reponse(input, image)
    st.markdown(response)

# if submit_btn:
#     model = create_gemini_model()
#     st.text(response)