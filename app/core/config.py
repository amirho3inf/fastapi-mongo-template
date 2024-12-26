from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import final, Optional


@final
class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=('.prod.env', '.dev.env', '.env'),
        env_file_encoding='utf-8',
        extra='ignore'
    )

    APP_TITLE: Optional[str] = "FastAPI"

    APP_SUMMARY: Optional[str] = "FastAPI with MongoDB"

    MONGODB_URI: str = "mongodb://127.0.0.1:27017/dbname"

    PROXY_URL: Optional[str] = None


cfg = Settings()
