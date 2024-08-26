import streamlit as st
from utils import extract_text_from_pdf
# from utils import preprocess_document, interact_with_gemini_api, analyze_results

st.title("Legal Document Analyzer with AI")
st.write("This tool helps you understand legal documents in simpler terms.")
st.subheader("Disclaimer: This is not a substitute for professional legal advice.")

uploaded_file = st.file_uploader("Upload a legal document (docx, pdf)", type=["docx", "pdf"])

if uploaded_file is not None:
    with st.spinner("Analyzing document"):
        st.write(extract_text_from_pdf(uploaded_file))