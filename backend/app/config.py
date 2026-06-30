from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "NexusOps Platform"
    api_prefix: str = "/api/v1"
    secret_key: str = "change-me-in-production-use-openssl-rand"
    access_token_expire_minutes: int = 60
    database_url: str = "sqlite:///./nexusops.db"
    cors_origins: list[str] = ["http://localhost:3000", "http://localhost:5173"]

    class Config:
        env_file = ".env"


settings = Settings()
