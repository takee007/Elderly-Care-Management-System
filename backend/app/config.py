import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Elderly Care Management System (ECMS)"
    PROJECT_VERSION: str = "1.0.0"
    API_V1_STR: str = "/api/v1"
    
    # Defaults to local SQLite, but seamlessly switchable to PostgreSQL via env var:
    # DATABASE_URL=postgresql://user:password@localhost:5432/ecms_db
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./ecms.db")
    
    SECRET_KEY: str = os.getenv("SECRET_KEY", "ecms_super_secret_jwt_key_2026_elderly_care_dev")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24  # 24 hours

settings = Settings()
