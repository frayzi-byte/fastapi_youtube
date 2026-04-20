import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DB_DIR = "data"
DB_FILE = "app.db"

os.makedirs(DB_DIR, exist_ok=True)

DATABASE_URL = f"sqlite:///{DB_DIR}/{DB_FILE}"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_tread" : False},
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

db = SessionLocal

Base = declarative_base


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()