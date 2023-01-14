from typing import List

from pydantic import BaseModel
from datetime import date


class PlaceWork(BaseModel):
    name: str
    city: str
    number_of_years: int


class User(BaseModel):
    first_name: str
    last_name: str
    age: int
    address: str
    birthdate: date
    work_experience: List[PlaceWork]


class Family(BaseModel):
    is_married: bool
    number_of_child: int = 0
