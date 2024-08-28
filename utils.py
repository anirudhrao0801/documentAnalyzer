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
        return text
    except Exception as e:
        print(f"Error extracting text from PDF:{e}")
        return None

def generate_response(text, pov_text):
    prompt = f"""Summarize the following legal document:

                {text}

                Point of view: {pov_text} 
                Please summarise it like you are explaining what I am liable for from my point of view
                In your summary, please:
                * Identify the key terms and conditions of the agreement.
                * Highlight any potential liabilities or obligations that the user is assuming.
                * Provide a concise overview of the user's rights and responsibilities.

                Please ensure that your summary is clear, concise, and easy to understand.
                """


    if GEMINI_API_KEY is not None:
        genai.configure(api_key=GEMINI_API_KEY)
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(prompt)
        return(response.text)
    else:
        return("API_KEY not specified!")
    

    

