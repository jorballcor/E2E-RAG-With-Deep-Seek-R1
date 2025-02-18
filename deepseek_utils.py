from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import requests
import os

from config import DOCUMENT_VECTOR_DB, LANGUAGE_MODEL, PDF_STORAGE_PATH, PROMPT_TEMPLATE


def save_uploaded_file(uploaded_file):
    file_path = os.path.join(PDF_STORAGE_PATH, uploaded_file.name)
    with open(file_path, "wb") as file:
        file.write(uploaded_file.getbuffer())
    return file_path


def load_pdf_documents(file_path):
    document_loader = PyPDFLoader(file_path)
    return document_loader.load()


def chunk_documents(raw_documents):
    text_processor = RecursiveCharacterTextSplitter(
        chunk_size=1000, chunk_overlap=200, add_start_index=True
    )
    return text_processor.split_documents(raw_documents)


def index_documents(document_chunks):
    DOCUMENT_VECTOR_DB.add_documents(document_chunks)


def find_related_documents(query):
    return DOCUMENT_VECTOR_DB.similarity_search(query)


def generate_answer(user_query, context_documents):
    context_text = "\n\n".join([doc.page_content for doc in context_documents])
    prompt = PROMPT_TEMPLATE.format(
        user_query=user_query, document_context=context_text
    )

    url = "http://127.0.0.1:1234/v1/chat/completions"
    headers = {"Content-Type": "application/json"}
    data = {
        "model": LANGUAGE_MODEL,
        "messages": [{"role": "system", "content": prompt}],
        "temperature": 0.3,
    }

    # Realiza la solicitud HTTP
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return "Error: Failed to generate response from LM Studio."
