from flask import Blueprint, request

from src import (
    constants,
    status,
    usecases
)
from src.adapters import log, Log
from src.helpers import response


health_bp = Blueprint("health", __name__, url_prefix="/health")

@health_bp.route("/check", methods=["GET"])
def check():
    try:
        usecases.health.check()
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

        return response.default(None, status.HTTP_NO_CONTENT)
    except Exception as e:
        log(Log(
            message="error to health check",
            method=request.method,
            reason=f"{e}",
            remote_ip=request.host,
            request_data=None,
            response_data=None,
            status_code=status.HTTP_INTERNAL_SERVER_ERROR,
            severity=constants.SEVERITY_ERROR,
            url_path=request.full_path,
        ))

        return response.default("error to health check", status.HTTP_INTERNAL_SERVER_ERROR)