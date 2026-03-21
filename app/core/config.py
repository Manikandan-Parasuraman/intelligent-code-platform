from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "AI Code Assistant"
    VECTOR_DB_PATH: str = "data/vector_store"
    REPO_PATH: str = "repo/"
    MODEL_NAME: str = "codellama"
    EMBEDDING_MODEL: str = "all-minilm"
    OLLAMA_BASE_URL: str = "http://ollama:11434"

settings = Settings()