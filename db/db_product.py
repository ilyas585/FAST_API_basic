from typing import Optional
from sqlalchemy.orm import Session

from db.models import Product
from api.product.schemas import Dimension


def get_product_by_id(db_session: Session, product_id: int) -> Optional[Product]:  # Product | None
    return db_session.query(Product).filter_by(id=product_id).first()


def get_products_by_name(db_session: Session, product_name: str) -> list[Product]:
    return db_session.query(Product).filter_by(name=product_name).all()


def get_all_products(db_session: Session) -> list[Product]:
    products = db_session.query(Product).all()
    return products


def create_product(db_session: Session, name: str, price: float, dimensions: Dimension) -> Product:
    product = Product(name=name, price=price, dimensions=dimensions)
    db_session.add(product)  # CREATE
    db_session.commit()
    db_session.refresh(product)  # refresh, add id to user
    return product


def update_product(db_session: Session, product_id: int, new_product):
    old_pr = get_product_by_id(db_session, product_id)  # UPDATE
    if old_pr is not None:
        old_pr.name = new_product.name if new_product.name is not None else old_pr.name
        old_pr.price = new_product.price if new_product.price is not None else old_pr.price
        old_pr.dimensions = new_product.dimensions if new_product.dimensions is not None else old_pr.dimensions
        db_session.commit()
        db_session.refresh(old_pr)
        return old_pr


def delete_product(db_session: Session, product_id: int) -> bool:
    product = get_product_by_id(db_session, product_id)
    if product:
        db_session.delete(product)  # DELETE
        db_session.commit()
        return True
    else:
        return False
