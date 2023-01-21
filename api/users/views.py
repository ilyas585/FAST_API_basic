from typing import List

from fastapi import APIRouter

from api.users import crud
from api.users.schemas import UserIn, UserOut, UserInPut


router_user = APIRouter(prefix="/user", tags=["User"])


@router_user.post("", response_model=UserOut)
def create_user(user_in: UserIn) -> UserOut:
    return crud.create_user(user_in)


@router_user.get("/{user_id}", response_model=UserOut)
def get_user_by_id(user_id: int, token: str) -> UserOut:
    crud.check_token(token)
    return crud.get_user_by_id(user_id)


@router_user.get("s", response_model=List[UserOut])
def get_users(token: str) -> List[UserOut]:
    crud.check_token(token)
    return crud.get_users()


@router_user.delete("/{user_id}")
def get_user_by_id(user_id: int, token: str) -> None:
    crud.check_token(token)
    return crud.delete_user(user_id)


@router_user.put("/{user_id}")
def put_user(user_id: int, user_in: UserInPut, token: str) -> UserOut:
    crud.check_token(token)
    return crud.put_user(user_id, user_in)
