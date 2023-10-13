from datetime import datetime

from src import adapters
from src.models.health import Health


def get():
    return adapters.sql.get_one("""
        SELECT *
        FROM public.health
        ORDER BY sync DESC
        LIMIT 1
    """, data_to=Health)

def insert(date: datetime):
    adapters.sql.insert("INSERT INTO public.health (sync) VALUES(:date) RETURNING sync", {"date": date}, True)
