# app/config.py

import os
from dotenv import load_dotenv
from urllib.parse import quote_plus

# Load .env at import time
load_dotenv()

class Config:
    # Flask
    SECRET_KEY = os.getenv("SECRET_KEY")
    
    # PostgreSQL — no hard-coded defaults
    DB_USER     = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_HOST     = os.getenv("DB_HOST", "db")
    DB_PORT     = os.getenv("DB_PORT", "5432")
    DB_NAME     = os.getenv("DB_NAME")

    # Make sure nothing’s missing
    for var in ("SECRET_KEY", "DB_USER", "DB_PASSWORD", "DB_NAME"):
        if not locals()[var]:
            raise RuntimeError(f"Environment variable {var} is required but not set.")

    # URL-encode the password
    _pw = quote_plus(DB_PASSWORD)

    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{DB_USER}:{_pw}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
