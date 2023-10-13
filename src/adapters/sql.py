from sqlalchemy import text, CursorResult

from flask import current_app

def get_one(query:str, params: dict = {}, data_to=dict):
    with current_app.config['DB'].connect() as conn:
        rs: CursorResult = conn.execute(text(query), params)
        conn.commit()
        try:
            return data_to(**rs.fetchone()._asdict())
        except AttributeError:
            return data_to({})

def get_all(query:str, params: dict = {}, data_to=dict):
    with current_app.config['DB'].connect() as conn:
        rs: CursorResult = conn.execute(text(query), params)
        conn.commit()
        rs = rs.fetchall()
        return [data_to(**obj._asdict()) for obj in rs]

def insert(query: str, params: dict = {}, returning=False):
    with current_app.config['DB'].connect() as conn:
        if not returning:
            conn.execute(text(query), params)
            conn.commit()
        else:
            rs: CursorResult = conn.execute(text(query), params)
            conn.commit()
            return rs.fetchone()._asdict()

def update(query: str, params: dict = {}, returning=False):
    with current_app.config['DB'].connect() as conn:
        if not returning:
            conn.execute(text(query), params)
            conn.commit()
        else:
            rs: CursorResult = conn.execute(text(query), params)
            conn.commit()
            return rs.fetchone()._asdict()