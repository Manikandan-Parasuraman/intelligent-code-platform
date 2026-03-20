from langchain.llms import Ollama
from app.core.config import settings


def get_llm():
    return Ollama(model=settings.MODEL_NAME)