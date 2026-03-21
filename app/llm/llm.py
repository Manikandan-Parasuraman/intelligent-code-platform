from langchain_ollama import OllamaLLM as Ollama
from app.core.config import settings


def get_llm(json_mode=False):
    if json_mode:
        return Ollama(model=settings.MODEL_NAME, base_url=settings.OLLAMA_BASE_URL, format="json")
    return Ollama(model=settings.MODEL_NAME, base_url=settings.OLLAMA_BASE_URL)