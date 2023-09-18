from google.cloud import logging
from google.cloud.logging_v2 import Resource

from src import constants


def cloud_log(payload: dict, severity: str):

    client = logging.Client()
    logger = client.logger(constants.LOGGER_NAME, resource=Resource("api", {"service": constants.LOGGER_SERVICE_NAME}))

    logger.log_struct(payload, severity=severity)