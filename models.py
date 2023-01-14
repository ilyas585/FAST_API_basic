from typing import List

from pydantic import BaseModel, Field, validator
from datetime import date


class PlaceWork(BaseModel):
    name: str = Field(None, max_length=128, title="name of company", description="full name")
    city: str
    number_of_years: int = Field(..., ge=0)

    @validator("city")
    def check_city(cls, value):
        if len(value) > 128:
            raise ValueError("City must be less than 128 symbols")
        if value not in ["Moscow", "Ankara", "Nalchik"]:
            raise ValueError(f"{value} is not city")

        return value


class Family(BaseModel):
    is_married: bool
    number_of_child: int = 0


class UserRequest(BaseModel):
    first_name: str = Field(..., description="first name of user")
    last_name: str
    age: int
    address: str
    birthdate: date
    work_experience: List[PlaceWork]


class UserResponse(UserRequest):
    id: int
    email: str
    family: Family
