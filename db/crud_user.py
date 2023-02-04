from typing import Optional, Type

from session import db_session, User, Product


def get_user_by_id(user_id) -> Optional[Type[User]]:
    return db_session.query(User).filter_by(id=user_id).first()  # for unique field


def get_users_by_username(username) -> list:
    return db_session.query(User).filter_by(username=username).all()  # for not unique field


def get_all_users():
    users = db_session.query(User).all()  # READ
    return users


def create_user(username=None, age=None, address=None, accessed_catalog=None):
    user = User(username=username, age=age, address=address, accessed_catalog=accessed_catalog)
    db_session.add(user)  # CREATE
    db_session.commit()


def update_user(user_id, new_user):
    old_user = get_user_by_id(user_id)  # UPDATE
    if old_user is not None:
        old_user.username = new_user.username if new_user.username is not None else old_user.username
        old_user.age = new_user.age if new_user.age is not None else old_user.age
        old_user.address = new_user.address if new_user.address is not None else old_user.address
        db_session.commit()
    else:
        return "not found"


def delete_user(user):
    db_session.delete(user)  # DELETE
    db_session.commit()


print(get_all_users())
# user1 = get_users_by_username("Vladimir")[0]
# delete_user(user1)
# print(get_all_users())
create_user("ivan", 15, "Novosibirsk", {"name": "one", "catalog": "food"})
print(get_all_users())
# user2 = User(age=90)
# update_user(99, user2)
#
# update_user(1, User(address="Ankara"))
#
# session.close()
