import os
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from PyPDF2 import PdfReader

# Initialize LLM with your API key
llm = ChatOpenAI(temperature=0, openai_api_key="your-open-ai-api-key", model="gpt-3.5-turbo")

def read_pdf(file_path):
    """Extract text from a PDF file."""
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def summarize_text(text):
    """Generate a concise 150-word summary from the document text."""
    prompt = PromptTemplate.from_template(
        "Summarize the following document in no more than 150 words:\n{context}"
    )
    chain = LLMChain(llm=llm, prompt=prompt)
    result = chain.run({"context": text})
    return result

def answer_question(text, question):
    """Answer a question about the document with reasoning and justification."""
    prompt = PromptTemplate.from_template(
        "Use the document content to answer the following:\nDocument: {context}\n"
        "Question: {question}\n\nProvide a detailed answer with reasoning and justification from the document."
    )
    chain = LLMChain(llm=llm, prompt=prompt)
    result = chain.run({"context": text, "question": question})
    return result

def generate_logic_questions(text):
    """Generate 3 reasoning or comprehension-based questions derived from the document."""
    prompt = PromptTemplate.from_template(
        "Read the following document and create 3 reasoning or logic-based questions from it.\n"
        "Provide numbered questions only, no answers.\n\nDocument:\n{context}"
    )
    chain = LLMChain(llm=llm, prompt=prompt)
    result = chain.run({"context": text})
    return result






