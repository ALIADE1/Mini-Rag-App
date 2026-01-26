from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str
    APP_VERSION: str
    OPEN_API_KEY: str

    FILE_ALLOWED_TYPES: list
    MAX_FILE_SIZE_MB: int

    class Config:
        env_file = ".env"


def Get_Settings():
    return Settings()
