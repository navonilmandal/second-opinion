from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional

class Settings(BaseSettings):
    APP_NAME: str = "Insurance Policy Review"
    APP_ENV: str = "development"
    DEBUG: bool = True
    
    # API Settings
    API_V1_STR: str = "/api/v1"
    
    # Auth
    JWT_SECRET_KEY: str
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    JWT_REFRESH_TOKEN_EXPIRE_DAYS: int = 7
    
    # DB & Redis
    DATABASE_URL: str
    REDIS_URL: str
    
    # Vector DB
    VECTOR_DB_URL: str
    VECTOR_DB_API_KEY: Optional[str] = None
    
    # Providers
    LLM_PROVIDER: str = "mock"
    LLM_API_KEY: Optional[str] = None
    LLM_MODEL: str = "google/gemini-1.5-flash"
    
    EMBEDDING_PROVIDER: str = "mock"
    EMBEDDING_API_KEY: Optional[str] = None
    EMBEDDING_MODEL: str = "embedding-001"
    
    # Storage
    STORAGE_PROVIDER: str = "local"
    S3_BUCKET: Optional[str] = None
    AWS_ACCESS_KEY_ID: Optional[str] = None
    AWS_SECRET_ACCESS_KEY: Optional[str] = None
    
    model_config = SettingsConfigDict(
        env_file=".env", 
        env_file_encoding="utf-8",
        extra="ignore"
    )

settings = Settings()
