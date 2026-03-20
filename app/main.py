from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="Enterprise AI Code Assistant")
app.include_router(router)

