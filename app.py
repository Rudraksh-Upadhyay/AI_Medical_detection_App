import streamlit as st 
from pathlib import Path
import google.generativeai as genai
from PIL import Image

#from api_key import api_key

GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel("gemini-2.0-flash")

#front end
st.set_page_config(page_title="Vital Image Analytics", page_icon=":robot:")
st.image("https://static.vecteezy.com/system/resources/previews/020/871/782/original/health-doctor-logo-medical-care-business-vector.jpg", width=150)
st.title("Vital Image Analytics")
st.subheader("An application that can help users to identify medical images")

uploaded_files = st.file_uploader("Upload the medical image for analysis", type=["png", "jpg", "jpeg"])

submit_button = st.button("Generate the Analysis")

if submit_button and uploaded_files is not None:
    image = Image.open(uploaded_files)
    
    st.image(image, caption="Uploaded Image", use_container_width=True)
    
    with st.spinner("Analyzing your image... ⏳"):
        
        response = model.generate_content(
            [
                "you are a medical assistant. Analyze this medical image and describe possible conditions, injuries, or abnormalities.Provide helpful gruidance in simple words.", image
            ]
        )
        
        st.success("Analysis Completed! 🎉")
        st.write(response.text)
