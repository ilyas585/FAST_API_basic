from pydantic import BaseModel, Field, validator


class ManufacturerBase(BaseModel):
    name: str = None
    address: str = None
    coefficient_sale: float = None


class ManufacturerIn(ManufacturerBase):
    pass


class ManufacturerOut(ManufacturerBase):
    id: int



