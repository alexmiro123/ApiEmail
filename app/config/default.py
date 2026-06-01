import os

class BaseConfig:
    SECRET_KEY = os.getenv("SECRET_KEY", "change-me")
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "change-me-jwt")
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # kept for compat with codebase

    DB_HOST = os.getenv("DB_HOST", "127.0.0.1")
    DB_PORT = os.getenv("DB_PORT", "1521")
    DB_SERVICE = os.getenv("DB_SERVICE", "ORCL")
    DB_USER = os.getenv("DB_USER", "REPORTES")
    DB_PASSWORD = os.getenv("DB_PASSWORD", "change-me")
    ORACLE_CLIENT_PATH = os.getenv("ORACLE_CLIENT_PATH", "")

class DefaultConfig(BaseConfig):
    pass
