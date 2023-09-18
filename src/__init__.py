import os

from flask import Flask, Blueprint
from flask_cors import CORS
from sqlalchemy import create_engine

from . import constants
from . import handlers


def __setup(app: Flask):
    allowed_origins = constants.ALLOWED_ORIGINS
    if os.getenv("ENVIRONMENT") != constants.ENVIRONTMENT_PRD:
        allowed_origins.extend(constants.ALLOWED_STG_ORIGINS)

    CORS(app, origins=allowed_origins, methods=["POST", "OPTIONS", "GET"])

def __route(app: Flask):
    api = Blueprint("api", __name__, url_prefix="/api")

    app.register_blueprint(api)
    app.register_blueprint(handlers.health_bp)


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config['DB'] = create_engine(f"postgresql://{os.getenv('DATABASE_URL')}", client_encoding="utf-8", implicit_returning=True)

    __setup(app)

    __route(app)

    return app