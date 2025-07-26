import os
from flask import Flask
from app.database import init_db

def create_app():
    app = Flask(__name__, static_folder='static')

    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    DB_PATH = os.path.join(BASE_DIR, '..', 'data', 'ecommerce.db')
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_PATH}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    init_db(app)

    from app.routes import main
    app.register_blueprint(main)

    return app