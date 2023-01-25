"""
Create
Read
Update
Delete
"""
from fastapi import HTTPException

from api.users.schemas import UserIn, UserOut, UserInPut
from api.users.helper import Helper


helper = Helper()


def check_token(token):
    if not isinstance(token, str):
        return {"message": "incorrect token", "details": "type is not string"}
    if not len(token.split('-')) == 5:
        return {"message": "incorrect token", "details": "token not with 5 blocks"}
    if token not in helper.cache_by_token:
        return {"message": "Authorization error", "details": "token not in cashe"}


def create_user(user_in: UserIn) -> UserOut:
    user = UserOut(**user_in.dict(), id=helper.next_id)
    helper.db[user.id] = user
    helper.cache_by_token[user.token] = user

    return user


def get_user_by_id(user_id: int, token: str) -> UserOut:
    errors = check_token(token)
    if errors is None:
        if user_id in helper.db:
            return helper.db[user_id]
        else:
            raise HTTPException(status_code=404, detail={"message": "User not found!"})
    else:
        raise HTTPException(status_code=400, detail=errors)


def get_users() -> list[UserOut]:
    user = list(helper.db.values())
    return user


def put_user(user_id: int, user_in: UserInPut) -> UserOut:
    user = helper.db[user_id].dict()
    for i, j in user_in.dict().items():
        if i in user and j is not None:
            user[i] = j

    user_out = UserOut(**user)
    helper.db[user_id] = user_out

    return user_out


def delete_user(user_id: int) -> None:
    if user_id in helper.db:
        del helper.db[user_id]
