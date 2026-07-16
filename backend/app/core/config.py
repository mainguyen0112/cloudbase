from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "CloudBase API"


settings = Settings()