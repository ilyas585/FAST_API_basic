import json  # builtin modules

from fastapi import FastAPI, Path, Query, Body  # external modules, i.o. which used pip install
from fastapi.responses import HTMLResponse, JSONResponse, FileResponse, RedirectResponse
import uvicorn

from models import UserRequest, UserResponse, Family  # custom modules, our self python files
from api.product.views import router_product


app = FastAPI()
app.include_router(router_product)


@app.get("/")
def home():
    return {"hello": "world"}


@app.get('/user/{user_id}')
def get_user_by_id(user_id: int = Path(..., gt=0, description="user id in DataBase"),
                   user_type: str = Query(..., max_length=15, description="user type"),
                   address: str = Query(None, min_length=3, description="address of user")):
    """
    :param user_id: is parameter of url (required-обязательно)
    :param user_type: is parameter of query (required-обязательно)
    :param address: is parameter of query (optional-необязательно)
    :return: simple json
    """
    return {'key': user_id, 'user_type': user_type, 'address': address}


@app.get("/user/check/{username}")
def check_username(username):
    if username not in ["alex", "ivan", "al123"]:
        return username


@app.post("/user", response_model=UserResponse, response_model_exclude={"address", "birthdate"})
def create_user(user: UserRequest, family: Family, email: str = Body(...)):
    if user.work_experience[0].number_of_years > user.age:
        return JSONResponse(status_code=400, content={"error": "number_of_years can't more than age"})

    return UserResponse(**user.dict(), id=100, family=family, email=email)


