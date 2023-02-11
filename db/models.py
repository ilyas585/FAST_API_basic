from sqlalchemy import Column, Integer, String, JSON, ARRAY
from sqlalchemy.orm import DeclarativeBase


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


class Token(Base):
    __tablename__ = "token"
    token = Column(String,  primary_key=True, unique=True)
    user_id = Column(Integer)

    def __repr__(self):
        return f"{self.user_id} {self.token}"


class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    name = Column(String(32), default=None)
    price = Column(Integer, default=None)
    # tags = Column(ARRAY(String), default=None)
    dimensions = Column(JSON, default=None)

    def __repr__(self):
        return f"{self.id} {self.price} {self.dimensions}"

