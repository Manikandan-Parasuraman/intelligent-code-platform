from langchain_community.vectorstores import FAISS
from langchain_ollama.embeddings import OllamaEmbeddings
from app.core.config import settings


def get_retriever():
    embeddings = OllamaEmbeddings(model=settings.MODEL_NAME)
    db = FAISS.load_local(settings.VECTOR_DB_PATH, embeddings, allow_dangerous_deserialization=True)
    return db.as_retriever(search_kwargs={"k": 5})