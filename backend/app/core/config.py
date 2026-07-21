from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    PROJECT_NAME: str = "DataLabs Demo"
    ENVIRONMENT: str = "development"

    # postgresql+asyncpg://user:password@host:port/datalabs_demo
    DATABASE_URL: str = "postgresql+asyncpg://password:username@localhost:5432/databasename"

    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    REFRESH_TOKEN_EXPIRE_DAYS: int = 14

    OAUTH_GOOGLE_CLIENT_ID: str | None = None
    OAUTH_GOOGLE_CLIENT_SECRET: str | None = None
    OAUTH_GITHUB_CLIENT_ID: str | None = None
    OAUTH_GITHUB_CLIENT_SECRET: str | None = None

    CORS_ORIGINS: list[str] = ["http://localhost:5173", "http://localhost:3000"]

    REDIS_URL: str = "redis://localhost:6379/0"


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
