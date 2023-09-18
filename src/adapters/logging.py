from dataclasses import dataclass
from typing import Union

from src.clients import google


@dataclass
class Log:
    message: str
    remote_ip: str
    request_data: Union[object,dict]
    response_data: Union[object,dict]
    severity: str
    method: str = None
    reason: str = None
    status_code: int = None
    url_path: str = None
    user: str = None


def log(payload: Log):
    severity = payload.severity
    payload = payload.__dict__
    del payload['severity']

    google.cloud_log(payload, severity)