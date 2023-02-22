from uuid import uuid4
from enum import Enum

from pydantic import BaseModel, Field, validator


class RoleEnum(str, Enum):
    admin = "admin"
    seller = "phones"
    expert = "expert"


class Employee(BaseModel):
    name: str
    role: RoleEnum


class EmployeeBase(BaseModel):
    name: str = None
    role: RoleEnum = None


class EmployeeIn(EmployeeBase):
    pass


class EmployeeOut(EmployeeBase):
    id: int

