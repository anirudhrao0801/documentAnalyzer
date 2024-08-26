import streamlit as st
import PyPDF2
from gemini_api_key import GEMINI_API_KEY
import google.generativeai as genai

def extract_text_from_pdf(pdf_file):
    """Extracts text from a PDF file.

    Args:
        pdf_file (bytes): The PDF file as bytes.

    Returns:
        str: The extracted text.
    """

    try:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        text = ""
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]

            text += page.extract_text()
        return text[0]
    except Exception as e:
        print(f"Error extracting text from PDF:{e}")
        return None

def generate_response():
    prompt = "Write me a story in 5 sentences"
    if GEMINI_API_KEY is not None:
        genai.configure(api_key=GEMINI_API_KEY)
        # defaults = {
        #             'model': 'models/text-bison-001',
        #             'temperature': 0.7,
        #             'candidate_count': 1,
        #             'top_k': 40,
        #             'top_p': 0.95,
        #             'max_output_tokens': 2048,
        #             'stop_sequences': [],
        #             'safety_settings': [{"category":"HARM_CATEGORY_DEROGATORY","threshold":1},{"category":"HARM_CATEGORY_TOXICITY","threshold":1},{"category":"HARM_CATEGORY_VIOLENCE","threshold":2},{"category":"HARM_CATEGORY_SEXUAL","threshold":2},{"category":"HARM_CATEGORY_MEDICAL","threshold":2},{"category":"HARM_CATEGORY_DANGEROUS","threshold":2}],
        #             }

        response = genai.generate_text(
            prompt=prompt
        )

        return response.result
    
    else:
        return (prompt, "")

    

