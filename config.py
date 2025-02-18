from langchain_core.vectorstores import InMemoryVectorStore
from langchain_huggingface import HuggingFaceEmbeddings


EMBEDDING_MODEL = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
DOCUMENT_VECTOR_DB = InMemoryVectorStore(embedding=EMBEDDING_MODEL)


PDF_STORAGE_PATH = 'pdfs/'
LANGUAGE_MODEL = 'deepseek-r1-distill-qwen-7b'
PROMPT_TEMPLATE = """
You are an expert research assistant. Use the provided context to answer the query. 
If unsure, state that you don't know. Be concise and factual (max 3 sentences).

Query: {user_query} 
Context: {document_context} 
Answer:
"""