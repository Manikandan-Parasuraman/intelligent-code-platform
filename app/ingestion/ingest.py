import os
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_ollama.embeddings import OllamaEmbeddings
from app.core.config import settings


def ingest():
    docs = []
    for root, _, files in os.walk(settings.REPO_PATH):
        for file in files:
            if file.endswith((".py", ".js", ".ts")):
                with open(os.path.join(root, file), encoding="utf-8") as f:
                    docs.append(f.read())

    print(f"Loading {len(docs)} documents...", flush=True)
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = splitter.create_documents(docs)

    print(f"Generating embeddings for {len(chunks)} chunks using {settings.EMBEDDING_MODEL}...", flush=True)
    embeddings = OllamaEmbeddings(model=settings.EMBEDDING_MODEL, base_url=settings.OLLAMA_BASE_URL)
    vector_store = FAISS.from_documents(chunks, embeddings)
    vector_store.save_local(settings.VECTOR_DB_PATH)
    print(f"Ingestion complete. Saved to {settings.VECTOR_DB_PATH}", flush=True)
    print("Ingestion complete.")


if __name__ == "__main__":
    ingest()