from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    port: int = Field(default=8080, alias="SCORE_SERVICE_PORT")
    log_level: str = Field(default="INFO", alias="SCORE_LOG_LEVEL")

    model_config = SettingsConfigDict(extra="ignore")
