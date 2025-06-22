from pydantic_settings import BaseSettings    
import os
from dotenv import load_dotenv

class Settings(BaseSettings):
    DB_NAME: str 
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: int

load_dotenv(".env")

settings = Settings()
DATABASE_URL = f'postgresql+asyncpg://{settings.DB_USER}:{settings.DB_PASSWORD}@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}'