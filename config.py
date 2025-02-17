from langchain_core.vectorstores import InMemoryVectorStore
from sentence_transformers import SentenceTransformer


EMBEDDING_MODEL = SentenceTransformer('all-MiniLM-L6-v2')
def generate_embeddings(text):
    return EMBEDDING_MODEL.encode(text)

DOCUMENT_VECTOR_DB = InMemoryVectorStore(embedding_function=generate_embeddings)


PDF_STORAGE_PATH = 'pdfs/'
LANGUAGE_MODEL = 'deepseek-r1-distill-qwen-7b'
PROMPT_TEMPLATE = """
You are an expert research assistant. Use the provided context to answer the query. 
If unsure, state that you don't know. Be concise and factual (max 3 sentences).

Query: {user_query} 
Context: {document_context} 
Answer:
"""