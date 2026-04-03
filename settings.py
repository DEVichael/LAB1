from pydantic_settings import BaseSettings
from pydantic import field_validator


class Settings(BaseSettings):
    ENVIRONMENT: str = "dev"
    APP_NAME: str = "My App"

    # Sekrety ładowane z environment variables
    api_key: str | None = None
    password: str | None = None

    @field_validator("ENVIRONMENT")
    @classmethod
    def validate_environment(cls, value):
        allowed = {"dev", "test", "prod"}
        if value not in allowed:
            raise ValueError(f"ENVIRONMENT must be one of {allowed}, got '{value}'")
        return value

    class Config:
        env_file = ".env"
