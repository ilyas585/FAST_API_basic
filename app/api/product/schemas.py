from pydantic import BaseModel
from typing import List


class Dimension(BaseModel):
    length: float
    width: float
    height: float


class ProductBase(BaseModel):
    name: str
    price: int
    # tags: List[str] = None
    dimensions: Dimension = None


class ProductIn(ProductBase):
    pass


class ProductInPut(ProductBase):
    name: str = None
    price: int = None


class ProductOut(ProductBase):
    id: int



