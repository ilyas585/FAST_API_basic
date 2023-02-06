from sqlalchemy import create_engine, Column, Integer, String, JSON, ARRAY
from sqlalchemy.orm import sessionmaker, scoped_session, DeclarativeBase

DB_URL = "sqlite:///basic_db.sqlite3"
engine = create_engine(url=DB_URL, echo=False)  # engine for connect application with DataBase
session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)


def db_session():
    db = Session()
    try:
        yield db  # return db, when finish job with db go ro finally
    finally:
        db.close()  # close session with db
