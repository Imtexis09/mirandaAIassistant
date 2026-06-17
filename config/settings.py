from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache

class Settings(BaseSettings):
    app_name: str = "Miranda AI Assistant"
    environment: str = "development"
    mode: str = "LOCAL"
    openai_api_key: str | None = None
    database_url: str = "sqlite:///./miranda.db"

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

@lru_cache()
def get_settings():
    return Settings()