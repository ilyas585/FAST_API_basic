"""
Create
Read
Update
Delete
"""
from typing import Type
from fastapi import HTTPException

from api.users.schemas import UserIn, UserOut, CreateUser
from db import db_user, db_token


class User:
    def __init__(self, db_session):
        self.db_session = db_session

    def check_token(self, token):
        if not isinstance(token, str):
            return {"message": "incorrect token", "details": "type is not string"}
        if not len(token.split('-')) == 5:
            return {"message": "incorrect token", "details": "token not with 5 blocks"}
        user = db_token.get_user_by_token(self.db_session, token)
        if user is None:
            return {"message": "Authorization error", "details": "token not in cache"}

    def create_user(self, user_in: UserIn) -> CreateUser:
        user = db_user.create_user(self.db_session, **user_in.dict())
        user_out = CreateUser(id=user.id, username=user.username, age=user.age, address=user.address,
                              accessed_catalog=user.accessed_catalog)
        db_token.add_token(self.db_session, user_out.id, user_out.token)
        return user_out

    def get_user_by_id(self, user_id: int, token: str):
        errors = self.check_token(token)
        if errors is None:
            user = db_user.get_user_by_id(self.db_session, user_id)
            if user:  # ==  if user is not None
                return UserOut(id=user.id, username=user.username, age=user.age, address=user.address,
                               accessed_catalog=user.accessed_catalog)
            else:
                raise HTTPException(status_code=404, detail={"message": "User not found!"})
        else:
            raise HTTPException(status_code=400, detail=errors)

    def get_users(self) -> [UserOut]:
        results = db_user.get_all_users(self.db_session)
        user_outs = []
        for u in results:
            uo = UserOut(id=u.id, age=u.age, username=u.username, address=u.address, accessed_catalog=u.accessed_catalog)
            user_outs.append(uo)
        return user_outs

    def put_user(self, user_id: int, user_in: UserIn) -> UserOut:
        user = db_user.update_user(self.db_session, user_id, user_in)
        if user:
            return UserOut(id=user.id, username=user.username, age=user.age, address=user.address,
                           accessed_catalog=user.accessed_catalog)
        else:
            raise HTTPException(status_code=404, detail={"message": "User not found!"})

    def delete_user(self, user_id: int) -> None:
        if not db_user.delete_user(self.db_session, user_id):
            raise HTTPException(status_code=404, detail={"message": "User not found!"})
