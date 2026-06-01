from app.extensions.db import acquire
from contextlib import contextmanager

def fetchone(query, params=None):
    params = params or {}
    with acquire() as conn:
        cur = conn.cursor()
        cur.execute(query, params)
        row = cur.fetchone()
        cur.close()
        return row

def fetchall(query, params=None):
    params = params or {}
    with acquire() as conn:
        cur = conn.cursor()
        cur.execute(query, params)
        rows = cur.fetchall()
        cur.close()
        return rows

def execute(query, params=None, commit=True):
    params = params or {}
    with acquire() as conn:
        cur = conn.cursor()
        cur.execute(query, params)
        if commit:
            conn.commit()
        lastrowid = None
        try:
            # attempt to get inserted id (if using RETURNING INTO)
            lastrowid = cur.lastrowid
        except Exception:
            lastrowid = None
        cur.close()
        return lastrowid


def fetchone_lob(query, params=None):
    params = params or {}

    with acquire() as conn:
        cur = conn.cursor()
        cur.execute(query, params)

        row = cur.fetchone()
        if not row:
            cur.close()
            return None

        value = row[0]

        if hasattr(value, "read"):
            value = value.read()

        cur.close()
        return value
