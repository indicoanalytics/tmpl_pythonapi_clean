from flask import Blueprint

communications_bp = Blueprint("communications", __name__, url_prefix="/communications")

@communications_bp.route('/email', methods=('POST'))
def email():
    print("email")

@communications_bp.route('/sms', methods=('POST'))
def sms():
    print('sms')