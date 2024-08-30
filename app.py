"""
i want to build an app that uses AI
probably sth with text input by the user
"""

import streamlit as st
from helper_functions import simplify_text, extract_text_from_pdf
import openai
import os
from PyPDF2 import PdfReader

# Initialize OpenAI API
openai.api_key = os.environ["OPENAI_API_KEY"]


# Streamlit app
st.title("PDF Language Simplifier")

# PDF file upload
pdf_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if pdf_file:
    # Extract text from PDF
    extracted_text = extract_text_from_pdf(pdf_file)
    
    if extracted_text:
        st.subheader("Original Text (First Few Pages)")
        st.text_area("Extracted Text", extracted_text, height=200)
        
        # Simplify the text using OpenAI
        if st.button("Simplify Text"):
            simplified_text = simplify_text(extracted_text)
            st.subheader("Simplified Text")
            st.text_area("Simplified Text", simplified_text, height=200)
    else:
        st.write("Unable to extract text from the PDF.")