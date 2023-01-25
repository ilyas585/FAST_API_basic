from typing import List

from fastapi import APIRouter

from api.product import crud
from api.product.schemas import ProductIn, ProductOut, ProductInPut


router_product = APIRouter(prefix="/product", tags=["Product"])


@router_product.post("", response_model=ProductOut)
def create_product(product_in: ProductIn, token: str) -> ProductOut:
    return crud.create_product(product_in, token)


@router_product.get("/{product_id}", response_model=ProductOut)
def get_product_by_id(product_id: int, token: str) -> ProductOut:
    return crud.get_product_by_id(product_id, token)


@router_product.get("s", response_model=List[ProductOut])
def get_products() -> List[ProductOut]:
    return crud.get_products()


@router_product.delete("/{product_id}")
def delete_product(product_id: int) -> None:
    return crud.delete_product(product_id)


@router_product.put("/{product_id}")
def put_product(product_id: int, product_in: ProductInPut) -> ProductOut:
    return crud.put_product(product_id, product_in)
