from flask import Blueprint, request, make_response

from src import constants, status
from src.usecases import health as health_usecase

from src.adapters import log, Log


health_bp = Blueprint("health", __name__, url_prefix="/health")

@health_bp.route("/check", methods=["GET"])
def check():
    health_usecase.check()

    log(Log(
        message="successfully health checked",
        method=request.method,
        remote_ip=request.host,
        request_data=None,
        response_data=None,
        status_code=status.HTTP_NO_CONTENT,
        severity=constants.SEVERITY_DEBUG,
        url_path=request.full_path,
    ))

    return make_response(), status.HTTP_NO_CONTENT