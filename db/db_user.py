from typing import Optional

from db.models import User


def get_user_by_id(db_session, user_id) -> Optional[User]:
    return db_session.query(User).filter_by(id=user_id).first()  # for unique field


def get_users_by_username(db_session, username) -> list:
    return db_session.query(User).filter_by(username=username).all()  # for not unique field


def get_all_users(db_session):
    users = db_session.query(User).all()  # READ
    return users


def create_user(db_session, username=None, age=None, address=None, accessed_catalog=None):
    user = User(username=username, age=age, address=address, accessed_catalog=accessed_catalog)
    db_session.add(user)  # CREATE
    db_session.commit()
    db_session.refresh(user)  # refresh, add id to user
    return user


def update_user(db_session, user_id, new_user):
    old_user = get_user_by_id(db_session, user_id)  # UPDATE
    if old_user is not None:
        old_user.username = new_user.username if new_user.username is not None else old_user.username
        old_user.age = new_user.age if new_user.age is not None else old_user.age
        old_user.address = new_user.address if new_user.address is not None else old_user.address
        old_user.accessed_catalog = new_user.accessed_catalog.dict() if new_user.accessed_catalog is not None else old_user.accessed_catalog
        db_session.commit()
        db_session.refresh(old_user)
        return old_user


def delete_user(db_session, user_id: int):
    user = get_user_by_id(db_session, user_id)
    if user:
        db_session.delete(user)  # DELETE
        db_session.commit()
        return True
    else:
        return False
