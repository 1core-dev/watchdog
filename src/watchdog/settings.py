from pydantic import BaseSettings
from dotenv import dotenv_values


class Settings(BaseSettings):
    server_host: str = '127.0.0.1'
    server_port: int = 5000
    db_url: str = 'sqlite:///./wd_db.sqlite3'
    # db_url: str = 'postgresql+psycopg2://user:password@localhost/db_test'


settings = Settings(
    _env_file='.env',
    _env_file_encoding='utf-8',
)
