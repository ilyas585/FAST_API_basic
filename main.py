import json  # builtin modules

from fastapi import FastAPI, Path, Query, Body  # external modules, i.o. which used pip install
import uvicorn

from models import User, Family  # custom modules, our self python files


app = FastAPI()


@app.get("/")
def home():
    return {"hello": "world"}


@app.get('/user/{user_id}')
def get_user_by_id(user_id: int = Path(..., gt=0, description="user id in DataBase"),
                   user_type: str = Query(..., max_length=15, description="user type"),
                   address: str = Query(None, min_length=3, description="address of user")):
    """
    :param user_id: is parameter of url (required-обязательно)
    :param user_type: is parameter of query (optional-необязательно)
    :param address: is parameter of query (optional-необязательно)
    :return: simple json
    """
    return {'key': user_id, 'user_type': user_type, 'address': address}


@app.post("/user")
def create_user(user: User, family: Family, email: str = Body(...)):
    return {"user": user, "family": family, "E-mail": email}
