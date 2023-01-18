"""
Create
Read
Update
Delete
"""

from api.product.schemas import ProductIn, ProductOut, ProductInPut
from api.product.helper import Helper


helper = Helper()


def create_product(product_in: ProductIn) -> ProductOut:
    product = ProductOut(**product_in.dict(), id=helper.next_id)
    helper.db[product.id] = product

    return product


def get_product_by_id(product_id: int) -> ProductOut:
    product = helper.db[product_id]
    return product


def get_products() -> list[ProductOut]:
    products = list(helper.db.values())
    return products


def put_product(product_id: int, product_in: ProductInPut) -> ProductOut:
    product = helper.db[product_id].dict()
    for i, j in product_in.dict().items():
        if i in product and j is not None:
            product[i] = j

    product_out = ProductOut(**product)
    helper.db[product_id] = product_out

    return product_out


def delete_product(product_id: int) -> None:
    if product_id in helper.db:
        del helper.db[product_id]
