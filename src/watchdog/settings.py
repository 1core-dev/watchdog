from pydantic import BaseSettings


class Settings(BaseSettings):
    server_host: str = '127.0.0.1'
    server_port: int = 5000
    db_url: str = 'sqlite:///./wd_db.sqlite3'

    jwt_secret: str
    jwt_algorithm: str = 'HS256'
    jwt_expiration: int = 86400


settings = Settings(
    _env_file='.env',
    _env_file_encoding='utf-8',
)
