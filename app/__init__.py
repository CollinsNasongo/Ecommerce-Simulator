from flask import Flask
from app.config import Config
from app.database import init_db

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    init_db(app)

    from app.routes import main
    app.register_blueprint(main)

    return app
