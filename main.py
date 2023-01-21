import json  # builtin modules

from fastapi import FastAPI, Path, Query, Body  # external modules, i.o. which used pip install
from fastapi.responses import HTMLResponse, JSONResponse, FileResponse, RedirectResponse
import uvicorn

from models import UserRequest, UserResponse, Family  # custom modules, our self python files
from api.product.views import router_product
from api.users.views import router_user


app = FastAPI()
app.include_router(router_product)
app.include_router(router_user)
