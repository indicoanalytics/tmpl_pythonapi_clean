from flask import Blueprint

communications_bp = Blueprint("communications", __name__, url_prefix="/communications")

@communications_bp.route('/email', methods=('POST'))
def email():
    if 1 == 1:
        print("init")