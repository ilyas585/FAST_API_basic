"""
Create
Read
Update
Delete
"""
from fastapi import HTTPException

from api.users.schemas import UserIn, UserOut, UserInPut
from db.session import db_session


def check_token(token):
    if not isinstance(token, str):
        return {"message": "incorrect token", "details": "type is not string"}
    if not len(token.split('-')) == 5:
        return {"message": "incorrect token", "details": "token not with 5 blocks"}
    if token not in db_session.cache_by_token:
        return {"message": "Authorization error", "details": "token not in cashe"}


def create_user(user_in: UserIn) -> UserOut:
    user = UserOut(**user_in.dict(), id=db_session.next_user_id)
    db_session.db_user[user.id] = user
    db_session.cache_by_token[user.token] = user

    return user


def get_user_by_id(user_id: int, token: str) -> UserOut:
    errors = check_token(token)
    if errors is None:
        if user_id in db_session.db_user:
            return db_session.db_user[user_id]
        else:
            raise HTTPException(status_code=404, detail={"message": "User not found!"})
    else:
        raise HTTPException(status_code=400, detail=errors)


def get_users(token: str) -> list[UserOut]:
    errors = check_token(token)
    if errors is None:
        return list(db_session.db_user.values())
    else:
        raise HTTPException(status_code=400, detail=errors)


def put_user(user_id: int, user_in: UserInPut) -> UserOut:
    user = db_session.db_user[user_id].dict()
    for i, j in user_in.dict().items():
        if i in user and j is not None:
            user[i] = j

    user_out = UserOut(**user)
    db_session.db_user[user_id] = user_out

    return user_out


def delete_user(user_id: int) -> None:
    if user_id in db_session.db_user:
        del db_session.db_user[user_id]
