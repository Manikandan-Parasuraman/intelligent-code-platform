from pydantic import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "AI Code Assistant"
    VECTOR_DB_PATH: str = "data/vector_store"
    REPO_PATH: str = "repo/"
    MODEL_NAME: str = "codellama"

settings = Settings()