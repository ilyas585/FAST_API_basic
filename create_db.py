"""
DB - is file for save data (file as tables)
SQL - language for request to DB

                    SQL & NOSQL
SQL (для постоянного хранения, обычно таблицы) - data of objects (users, products, address, devices)   [sqlite, postgresql, oracle]
NOSQL (для быстрого доступа, обычно формат json) - cash, tokens etc.   [Redis, MongoDB]

table users
id   username   address
1     alex       Moscow
2     Oleg       Nalchik

table products
id    name    price

-------------------------------------------------------------
sqlalchemy - for create tables, get data update data etc...
DBeaver
"""
from sqlalchemy import (
    create_engine,
    MetaData,
    Table,
    Column,
    Integer,
    String,
    FLOAT,
    JSON
)

DB_URL = "sqlite:///basic_db.sqlite3"
engine = create_engine(url=DB_URL, echo=True)  # engine for connect application with DataBase
metadata = MetaData()

user_table = Table(
    'users',
    metadata,
    Column("id", Integer, primary_key=True, unique=True, autoincrement=True),
    # primary_key - первичный ключ, unique - все id уникальный, autoincrement - авто назначение id
    Column("username", String),
    Column("age", Integer),
    Column("address", String),
    Column("accessed_catalog", JSON)
)

token_table = Table(
    "token",
    metadata,
    Column("token", String, primary_key=True, unique=True),
    Column("user_id", Integer)
)

product_table = Table(
    'products',
    metadata,
    Column("id", Integer, primary_key=True, unique=True, autoincrement=True),
    # primary_key - первичный ключ, unique - все id уникальный, autoincrement - авто назначение id
    Column("name", String),
    Column("price", FLOAT),
    # Column("tags", String),
    Column("dimensions", JSON)
)

metadata.create_all(bind=engine)
