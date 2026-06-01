import os
import oracledb
from flask import current_app
from contextlib import contextmanager

_pool = None

def init_db_pool(app=None):
    """
    Initialize a global connection pool. Call from create_app(app).
    """
    global _pool
    if _pool:
        return _pool

    # optionally init instant client if path provided
    client_path = os.getenv("ORACLE_CLIENT_PATH", "")
    if client_path:
        try:
            oracledb.init_oracle_client(lib_dir=client_path)
        except Exception as e:
            app.logger.warning(f"Could not init Oracle Instant Client: {e}")

      
    dsn = f"{app.config['DB_HOST']}:{app.config['DB_PORT']}/{app.config['DB_SERVICE']}"
    pool_min = 2
    pool_max = 10
    pool_inc = 1

    _pool = oracledb.create_pool(
        user=app.config["DB_USER"],
        password=app.config["DB_PASSWORD"],
        dsn=dsn,
        min=pool_min,
        max=pool_max,
        increment=pool_inc
    )


    if app:
        app.logger.info("Oracle connection pool created")
    return _pool

def get_pool():
    global _pool
    if not _pool:
        # attempt lazy init
        init_db_pool()
    return _pool

@contextmanager
def acquire():
    """
    Context manager that yields a connection and ensures release.
    Usage:
        with acquire() as conn:
            ...
    """
    pool = get_pool()
    conn = None
    try:
        conn = pool.acquire()
        yield conn
    finally:
        if conn:
            try:
                pool.release(conn)
            except Exception:
                conn.close()
