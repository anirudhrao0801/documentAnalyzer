import streamlit as st
import PyPDF2

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

def gener


    

