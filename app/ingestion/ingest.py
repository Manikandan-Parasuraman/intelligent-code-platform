import os
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings import OllamaEmbeddings
from app.core.config import settings


def ingest():
    docs = []
    for root, _, files in os.walk(settings.REPO_PATH):
        for file in files:
            if file.endswith((".py", ".js", ".ts")):
                with open(os.path.join(root, file), encoding="utf-8") as f:
                    docs.append(f.read())

    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = splitter.create_documents(docs)

    embeddings = OllamaEmbeddings(model=settings.MODEL_NAME)
    db = FAISS.from_documents(chunks, embeddings)
    db.save_local(settings.VECTOR_DB_PATH)