from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    NEWS_API_KEY: str
    CLIENT_ID: str
    CLIENT_SECRET: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    DATABASE_URL: str

    model_config = {
        "env_file": ".env",
        "env_file_encoding": "utf-8",
    }


settings = Settings()
