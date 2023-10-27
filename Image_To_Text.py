import streamlit as st
from PIL import Image
import easyocr
import tempfile

st.title("Image to Text Converter")
# Upload an image
uploaded_image = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

if uploaded_image is not None:
    image = Image.open(uploaded_image)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Save the uploaded image as a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as temp_image:
        image.save(temp_image.name, format="PNG")

    # Perform OCR on the image using easyocr
    reader = easyocr.Reader(['en'])  # Initialize the OCR reader with English language support
    text = reader.readtext(temp_image.name)

    # Extract and display the text
    extracted_text = ' '.join([result[1] for result in text])

    st.subheader("Extracted Text:")
    st.write(extracted_text)
