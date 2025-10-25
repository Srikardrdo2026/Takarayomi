from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from config import Config

engine = create_engine(Config.SQLALCHEMY_DATABASE_URI, echo=False, future=True)
Session = sessionmaker(autocommit = False, bind=engine, autoflush = False)
Base = declarative_base()

def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()