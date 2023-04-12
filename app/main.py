from fastapi import FastAPI
from app.api.product.views import router_product
from app.api.users.views import router_user
from app.api.employee.views import router_employee
from app.api.manufacturer.views import router_manufacturer

app = FastAPI()
app.include_router(router_product)
app.include_router(router_user)
app.include_router(router_employee)
app.include_router(router_manufacturer)


@app.get("/")
def root():
    return {"message": "Hello FAST_API"}


# uvicorn.run(app, host="0.0.0.0", port=80)

