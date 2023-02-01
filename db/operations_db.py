from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, FLOAT
from sqlalchemy.orm import sessionmaker, scoped_session, DeclarativeBase

DB_URL = "sqlite:///basic_db.sqlite3"
engine = create_engine(url=DB_URL, echo=False)  # engine for connect application with DataBase
session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)
session = Session()


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, unique=True)
    username = Column(String, default=None)
    age = Column(Integer, default=None)
    address = Column(String, default=None)

    def __repr__(self):
        return f"{self.id} {self.username}"


def get_user_by_id(user_id) -> User:
    return session.query(User).filter_by(id=user_id).first()  # for unique field


def get_users_by_username(username) -> list:
    return session.query(User).filter_by(username=username).all()  # for not unique field


def get_all_users():
    users = session.query(User).all()  # READ
    return users


def create_user(username, age, address):
    user = User(username=username, age=age, address=address)
    session.add(user)  # CREATE
    session.commit()


def update_user(user_id, new_user):
    old_user = get_user_by_id(user_id)  # UPDATE
    old_user.username = new_user.username if new_user.username is not None else old_user.username
    old_user.age = new_user.age if new_user.age is not None else old_user.age
    old_user.address = new_user.address if new_user.address is not None else old_user.address
    session.commit()


def delete_user(user):
    session.delete(user)  # DELETE
    session.commit()


# print(get_all_users())
# user1 = get_users_by_username("Vladimir")[0]
# delete_user(user1)
print(get_all_users())
create_user("aleksandra", 55, "Moscow")
print(get_all_users())
user2 = User(age=90)
update_user(1, user2)

update_user(1, User(address="Ankara"))

session.close()
