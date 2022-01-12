from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .settings import settings

engine = create_engine(
    settings.db_url,
    echo=True,
    connect_args={'check_same_thread': False},
)

Session = sessionmaker(
    engine,
    autoflush=False,
    autocommit=False,
)
