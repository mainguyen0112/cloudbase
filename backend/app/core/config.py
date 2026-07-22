from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    # App
    app_name: str = "CloudBase API"
    app_version: str = "0.1.0"
    debug: bool = False

    # Database
    database_url: str

    # AWS
    aws_region: str = "ap-southeast-1"
    s3_bucket: str = "cloudbase-recipe-images"


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()