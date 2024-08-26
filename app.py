import streamlit as st
from utils import extract_text_from_pdf, generate_response
# from utils import preprocess_document, interact_with_gemini_api, analyze_results

# Styling
st.set_page_config(
    page_title="Legal Document Analyzer",
    page_icon="⚖️",  # A scale of justice emoji
)

# Custom CSS for dark mode
st.markdown(
    """
    <style>
    .stApp {
        font-family: Arial, sans-serif;
        background-color: #181818;
    }
    .st-container {
        padding: 20px;
    }
    .st-h1 {
        color: #f5f5f5;
    }
    .st-text {
        color: #d9d9d9;
    }
    .st-button {
        background-color: #333333;
        color: #f5f5f5;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Main content
st.title("Legal Document Analyzer")
st.write("This tool helps you understand legal documents in simpler terms.")
st.subheader("Disclaimer: This is not a substitute for professional legal advice.")

uploaded_file = st.file_uploader("Upload a legal document (docx, pdf)", type=["docx", "pdf"])
analyze_button = st.button("Analyze Document")
if uploaded_file is not None and analyze_button:
    with st.spinner("Analyzing document"):
        if extract_text_from_pdf(uploaded_file):
            st.write(generate_response())