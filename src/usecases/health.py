from datetime import datetime

from src import constants, repository


def __check_database():
    now = datetime.utcnow().isoformat()

    repository.health.insert(now)

    health = repository.health.get()

    health.sync = health.sync.isoformat().split("+")[0]
    if health.sync < now or health.sync > now:
        raise Exception(constants.ERR_OUT_OF_SYNC)

def check():
    __check_database()