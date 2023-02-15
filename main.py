from fastapi import FastAPI
from api.product.views import router_product
from api.users.views import router_user

import uvicorn

app = FastAPI()
app.include_router(router_product)
app.include_router(router_user)

# uvicorn.run(app)

