from api.users.schemas import UserOut
from api.product.schemas import ProductOut
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, FLOAT, JSON, ARRAY
from sqlalchemy.orm import sessionmaker, scoped_session, DeclarativeBase

DB_URL = "sqlite:///basic_db.sqlite3"
engine = create_engine(url=DB_URL, echo=False)  # engine for connect application with DataBase
session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    username = Column(String, default=None)
    age = Column(Integer, default=None)
    address = Column(String, default=None)
    accessed_catalog = Column(JSON, default=None)

    def __repr__(self):
        return f"{self.id} {self.username}"


class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    name = Column(String(32), default=None)
    price = Column(Integer, default=None)
    tags = Column(ARRAY(String), default=None)
    dimensions = Column(JSON, default=None)

    def __repr__(self):
        return f"{self.id} {self.price} {self.tags} {self.dimensions}"

#
# class Session:
#     def __init__(self):
#         self.db_user: dict[int, UserOut] = {}
#         self.db_product: dict[int, ProductOut] = {}
#         self.cache_by_token: dict[str, UserOut] = {}
#
#         self.current_user_id = 0
#         self.current_product_id = 0
#
#     @property
#     def next_user_id(self) -> int:
#         self.current_user_id += 1
#         return self.current_user_id
#
#     @property
#     def next_product_id(self) -> int:
#         self.current_product_id += 1
#         return self.current_product_id


db_session = Session()


