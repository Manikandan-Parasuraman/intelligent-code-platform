import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import router

app = FastAPI(title="Enterprise AI Code Assistant")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)

@app.get("/files")
def list_files():
    files = []
    for root, _, filenames in os.walk("repo/"):
        for f in filenames:
            files.append(f)
    return {"files": files}


@app.get("/file")
def get_file(name: str):
    path = f"repo/{name}"
    if not os.path.exists(path):
        return {"content": ""}
    
    with open(path, "r", encoding="utf-8") as f:
        return {"content": f.read()}