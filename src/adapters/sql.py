from sqlalchemy import text

from flask import current_app

def get_one(query:str, params: dict = {}):
    print(current_app)
    with current_app.config['DB'].connect() as conn:
        rs = conn.execute(text(query), **params)
        rs = rs.fetchone()
        return dict(rs) if rs else dict()

def get_all(query:str, params: dict = {}):
    with current_app.config['DB'].connect() as conn:
        rs = conn.execute(text(query), **params)
        rs = rs.fetchall()
        return [dict(obj) for obj in rs]

def insert(query: str, params: dict = {}, returning=False):
    with current_app.config['DB'].connect() as conn:
        if not returning: conn.execute(text(query), **params)
        else:
            rs = conn.execute(text(query), **params)
            rs = rs.fetchone()
            return dict(rs) if rs else dict()

def update(query: str, params: dict = {}, returning=False):
    with current_app.config['DB'].connect() as conn:
        if not returning: conn.execute(text(query), **params)
        rs = conn.execute(text(query), **params)
        rs = rs.fetchone()
        return dict(rs) if rs else dict()