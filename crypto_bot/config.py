from typing import Literal

from pydantic import BaseSettings


class Settings(BaseSettings):
    MODE: Literal["DEV", "TEST", "PROD"]
    BOT_TOKEN: str
    API_URL: str
    SECRET_KEY: str
    ALGORITHM: str
    TG_ADMIN_ID: str

    class Config:
        env_file = ".env"


settings = Settings()
