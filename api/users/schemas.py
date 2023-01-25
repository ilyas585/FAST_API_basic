from uuid import uuid4
from enum import Enum

from pydantic import BaseModel, Field, validator


class CatalogEnum(str, Enum):
    food = "food"
    phones = "phones"
    furniture = "furniture"
    vehicle = "vehicle"
    international_food = "international_food"


class Catalog(BaseModel):
    name: str
    catalog: CatalogEnum

    # @validator("catalog")
    # def check_catalog(cls, value):
    #     if value not in ["Food", "Furniture", "Vehicle"]:
    #         raise ValueError(f"{value} is not catalog")
    #
    #     return value


class UserBase(BaseModel):
    user_name: str
    age: int
    address: str
    accessed_catalog: Catalog = None


class UserIn(UserBase):
    pass


class UserInPut(UserBase):
    user_name: str = None
    age: int = None
    address: str = None


def generate_token():
    return str(uuid4())


class UserOut(UserBase):
    id: int
    token: str = Field(default_factory=generate_token)
