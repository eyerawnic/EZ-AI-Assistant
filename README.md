# SmartAssistantGenAI

##  Overview
An AI-powered document-aware assistant for summarizing, querying, and reasoning over uploaded research papers or reports in PDF/TXT format.

##  Features
- PDF/TXT document upload
- Auto summarization (≤150 words)
- Free-form question answering with document-grounded justifications
- 'Challenge Me' mode with 3 generated logic-based questions, answer validation, and reasoning
- Snippet highlighting in answers (Bonus)

##  Tech Stack
- Python (LangChain, PyPDF2, Transformers)
- Streamlit (frontend)
- FastAPI (backend API)

##  Project Structure
```
SmartAssistantGenAI/
├── backend/
├── frontend/
├── data/
├── utils/
├── README.md
```

##  Setup Instructions
1. Install requirements:
```
pip install -r requirements.txt
```

2. Run the Streamlit app:
```
streamlit run frontend/app.py
```

3. (Optional) Start backend API if separated.

##  Architecture
- Document uploaded via Streamlit
- Summarization & Q&A handled by LangChain + OpenAI/Llama
- Responses include document-based justifications

