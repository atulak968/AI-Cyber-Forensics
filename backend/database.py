from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# SQLite database
DATABASE_URL = "sqlite:///./cyber_forensics.db"

# Engine
engine = create_engine(
    DATABASE_URL,
    connect_args={
        "check_same_thread": False
    }
)

# Session
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Base
Base = declarative_base()