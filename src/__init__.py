import os

from flask import Flask, Blueprint
from flask_cors import CORS
from sqlalchemy import create_engine

from . import constants
from . import middleware
from . import handlers


def route(app: Flask):
    api = Blueprint("api", __name__, url_prefix="/api")

    app.register_blueprint(api)
    app.register_blueprint(handlers.health_bp)

def set_default_handlers(app: Flask):
    app.before_request(middleware.setup)

    # TODO: Check how these work
    app.after_request(middleware.after_request)
    app.process_response(middleware.process_response)

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config['DB'] = create_engine(f"postgresql://{os.getenv('DATABASE_URL')}", client_encoding="utf-8", implicit_returning=True)

    route(app)
    set_default_handlers(app)


    return app