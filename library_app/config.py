from pydantic import BaseSettings
from dotenv import dotenv_values


class EnvVariables(BaseSettings):
    SQLITE_DATABASE_URL: str


secrets = EnvVariables(**dotenv_values("library_app/.env"))