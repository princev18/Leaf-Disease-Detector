
import streamlit as st
import numpy as np
from PIL import Image

st.set_page_config(
    page_title="PlantCare AI",
    page_icon="🌿",
    layout="wide"
)

st.title("🌿 PlantCare AI")
st.subheader("Plant Leaf Disease Detection & Treatment Recommender")

st.write(
    "Upload a plant leaf image to start the disease detection process."
)

uploaded_file = st.file_uploader(
    "Upload Leaf Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")

    st.image(
        image,
        caption="Uploaded Plant Leaf",
        width=350
    )

    st.info("Image uploaded successfully!")

    st.warning(
        "CNN model is not connected yet. "
        "Disease prediction will be enabled after model training."
    )

st.divider()

st.subheader("Project Workflow")

st.write("1. Upload a plant leaf image")
st.write("2. Resize and preprocess the image")
st.write("3. CNN model predicts the disease")
st.write("4. Display disease information")
st.write("5. Provide treatment guidance")

st.caption(
    "Academic project prototype | Python, TensorFlow and Streamlit"
)
