from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str = "Shopping List API"
    app_version: str = "1.0.0"
    port: int = 8000

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()