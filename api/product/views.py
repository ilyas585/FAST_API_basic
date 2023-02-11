from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from api.product import crud
from api.product.schemas import ProductIn, ProductOut, ProductInPut
from db.session import db_session

router_product = APIRouter(prefix="/product", tags=["Product"])


@router_product.post("", response_model=ProductOut)
def create_product(product_in: ProductIn, db: Session = Depends(db_session)) -> ProductOut:
    return crud.Product(db).create_product(product_in)


@router_product.get("/{product_id}", response_model=ProductOut)
def get_product_by_id(product_id: int, db: Session = Depends(db_session)) -> ProductOut:
    return crud.Product(db).get_product_by_id(product_id)


@router_product.get("s", response_model=List[ProductOut])
def get_products(db: Session = Depends(db_session)) -> List[ProductOut]:
    return crud.Product(db).get_products()


@router_product.delete("/{product_id}")
def delete_product(product_id: int, db: Session = Depends(db_session)) -> None:
    return crud.Product(db).delete_product(product_id)


@router_product.put("/{product_id}")
def put_product(product_id: int, product_in: ProductInPut, db: Session = Depends(db_session)) -> ProductOut:
    return crud.Product(db).put_product(product_id, product_in)
