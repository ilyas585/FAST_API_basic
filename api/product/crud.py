"""
Create
Read
Update
Delete
"""
from fastapi import HTTPException
from sqlalchemy.orm import Session

from api.product.schemas import ProductIn, ProductOut, ProductInPut
from db import db_product


class Product:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def create_product(self, product_in: ProductIn) -> ProductOut:
        product = db_product.create_product(self.db_session, **product_in.dict())
        product_out = ProductOut(id=product.id, name=product.name, price=product.price, dimensions=product.dimensions)
        return product_out

    def get_product_by_id(self, product_id: int):
        product = db_product.get_product_by_id(self.db_session, product_id)
        if product:  # ==  if user is not None
            return ProductOut(id=product.id, name=product.name, price=product.price, dimensions=product.dimensions)
        else:
            raise HTTPException(status_code=404, detail={"message": "Product not found!"})

    def get_products(self) -> list[ProductOut]:
        results = db_product.get_all_products(self.db_session)
        product_outs = []
        for p in results:
            po = ProductOut(id=p.id, name=p.name, price=p.price, dimensions=p.dimensions)
            product_outs.append(po)
        return product_outs

    def put_product(self, product_id: int, product_in: ProductInPut) -> ProductOut:
        product = db_product.update_product(self.db_session, product_id, product_in)
        if product:
            return ProductOut(id=product.id, name=product.name, price=product.price, dimensions=product.dimensions)
        else:
            raise HTTPException(status_code=404, detail={"message": "Product not found!"})

    def delete_product(self, product_id: int) -> None:
        if not db_product.delete_product(self.db_session, product_id):
            raise HTTPException(status_code=404, detail={"message": "Product not found!"})
