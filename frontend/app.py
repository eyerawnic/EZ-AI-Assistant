
import streamlit as st
import sys
import os

if not os.path.exists("data"):
    os.makedirs("data")

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'backend')))

from main import read_pdf, summarize_text, answer_question, generate_logic_questions

st.set_page_config(page_title="SmartAssistantGenAI")

st.title("📑 Smart Assistant for Document Summarization and Reasoning")

uploaded_file = st.file_uploader("Upload a PDF or TXT file", type=["pdf", "txt"])
if uploaded_file:
    file_path = os.path.join("data", uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.read())
    st.success(f"Uploaded: {uploaded_file.name}")

    if uploaded_file.name.endswith(".pdf"):
        doc_text = read_pdf(file_path)
    else:
        with open(file_path, "r") as f:
            doc_text = f.read()

    st.subheader("📄 Auto Summary")
    summary = summarize_text(doc_text)
    st.write(summary)

    mode = st.radio("Select Mode", ["Ask Anything", "Challenge Me"])

    if mode == "Ask Anything":
        query = st.text_input("Ask a question about the document")
        if st.button("Get Answer"):
            response = answer_question(doc_text, query)
            st.write(response)

    elif mode == "Challenge Me":
        st.subheader("🧠 Challenge Questions")
        questions = generate_logic_questions(doc_text)
        st.write(questions)
