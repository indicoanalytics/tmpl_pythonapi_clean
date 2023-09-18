from datetime import datetime

from src import adapters
from src.models.health import Health


def get():
    return Health(**adapters.sql.get_one("""
        SELECT *
        FROM public.health
        ORDER BY sync DESC
        LIMIT 1
    """))

def insert(date: datetime):
    adapters.sql.insert("INSERT INTO public.health (sync) VALUES(:date)", {"date": date})
