from enum import Enum

from pydantic import BaseModel


class RoleEnum(str, Enum):
    admin = "admin"
    seller = "seller"
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

