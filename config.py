import os

class Config:
    # Set the path for the SQLite database
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))  # Get the absolute path to the config directory
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{os.path.join(BASE_DIR, "../data/ecommerce.db")}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Disable modification tracking for performance
