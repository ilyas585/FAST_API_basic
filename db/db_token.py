from typing import Optional, Type

from db.models import User, Token


def get_user_by_token(db_session, token: str) -> Optional[Type[User]]:
    return db_session.query(Token).filter_by(token=token).first()  # for unique field


def add_token(db_session, user_id: int, token: str):
    token = Token(user_id=user_id, token=token)
    db_session.add(token)
    db_session.commit()
    db_session.refresh(token)
    print(token)
