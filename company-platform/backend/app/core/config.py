from functools import lru_cache
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict
class Settings(BaseSettings):
    app_name: str = "AXLWORKS Company Platform"
    app_env: str = "development"
    database_url: str
    jwt_secret_key: str = Field(min_length=32)
    jwt_access_token_minutes: int = Field(default=15, ge=5, le=60)
    ceo_bootstrap_email: str = ""
    ceo_bootstrap_password: str = ""
    cors_origins: str = "http://localhost:3001"
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")
    @property
    def cors_origin_list(self) -> list[str]:
        return [v.strip() for v in self.cors_origins.split(",") if v.strip()]
@lru_cache
def get_settings() -> Settings:
    return Settings()
settings = get_settings()
