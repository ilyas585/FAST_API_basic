from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from api.users import crud
from api.users.schemas import UserIn, UserOut, CreateUser
from db.session import db_session


router_user = APIRouter(prefix="/user", tags=["User"])


@router_user.post("", response_model=CreateUser)
def create_user(user_in: UserIn, db: Session = Depends(db_session)) -> CreateUser:
    return crud.User(db).create_user(user_in)


@router_user.get("/{user_id}", response_model=UserOut)
def get_user_by_id(user_id: int, token: str, db: Session = Depends(db_session)) -> UserOut:
    return crud.User(db).get_user_by_id(user_id, token)


@router_user.get("s", response_model=List[UserOut])
def get_users(db: Session = Depends(db_session)) -> List[UserOut]:
    return crud.User(db).get_users()


@router_user.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(db_session)) -> None:
    return crud.User(db).delete_user(user_id)


@router_user.put("/{user_id}")
def put_user(user_id: int, user_in: UserIn, db: Session = Depends(db_session)) -> UserOut:
    return crud.User(db).put_user(user_id, user_in)
