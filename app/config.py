import os
from dotenv import load_dotenv
from urllib.parse import quote_plus

# Load environment variables from .env
load_dotenv()

class Config:
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = quote_plus(os.getenv("DB_PASSWORD"))  
    DB_HOST = os.getenv("DB_HOST", "localhost")
    DB_PORT = os.getenv("DB_PORT", "5432")
    DB_NAME = os.getenv("DB_NAME")

    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
