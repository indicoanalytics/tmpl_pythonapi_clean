import os

from flask import Blueprint, Flask
from flask_cors import CORS
from sqlalchemy import create_engine

from . import constants, handlers, middleware


def route(app: Flask):
    app.register_blueprint(handlers.health_bp)

    api = Blueprint("api", __name__, url_prefix="/api")

    if os.getenv("ENVIRONMENT") != constants.ENVIRONMENT_PRD:
        constants.ALLOWED_ORIGINS.extend(constants.ALLOWED_STG_ORIGINS)

    CORS(api, methods=constants.ALLOWED_ORIGINS)

    app.register_blueprint(api)

def set_default_handlers(app: Flask):
    app.after_request(middleware.after_request)

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config['DB'] = create_engine(f"postgresql://{os.getenv('DATABASE_URL')}", client_encoding="utf-8", implicit_returning=True)

    route(app)
    set_default_handlers(app)


    return app