from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from pulse_watch.db.base import Base
from pulse_watch.models import Monitor

from pulse_watch.core.config import settings

engine = create_engine(
    settings.database_url,
    connect_args={"check_same_thread": False}
    if settings.database_url.startswith("sqlite")
    else {}
)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)

def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()

def init_db():
    Base.metadata.create_all(bind=engine)