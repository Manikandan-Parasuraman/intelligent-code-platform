from langchain_community.vectorstores import FAISS
from langchain_ollama.embeddings import OllamaEmbeddings
from app.core.config import settings


def get_retriever():
    embeddings = OllamaEmbeddings(model=settings.EMBEDDING_MODEL, base_url=settings.OLLAMA_BASE_URL)
    print(f"Query Dim: {len(embeddings.embed_query('test'))}", flush=True)
    db = FAISS.load_local(settings.VECTOR_DB_PATH, embeddings, allow_dangerous_deserialization=True)
    print(f"Index dimension: {db.index.d}", flush=True)
    return db.as_retriever(search_kwargs={"k": 5})