import os

from flask import Flask, Blueprint

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    # TODO: declare routes from here.
    import handlers

    api = Blueprint("api", __name__, url_prefix="/api")
    api.register_blueprint(handlers.communications_bp)


    app.register_blueprint(api)
    
    return app