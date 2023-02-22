from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from api.employee import crud
from api.employee.schemas import EmployeeIn, EmployeeOut
from db.session import db_session

router_employee = APIRouter(prefix="/employee", tags=["employee"])


@router_employee.post("", response_model=EmployeeOut)
def create_employee(employee_in: EmployeeIn, db: Session = Depends(db_session)) -> EmployeeOut:
    return crud.Employee(db).create_employee(employee_in)


@router_employee.get("/{employee_id}", response_model=EmployeeOut)
def get_employee_by_id(employee_id: int, db: Session = Depends(db_session)) -> EmployeeOut:
    return crud.Employee(db).get_employee_by_id(employee_id)


@router_employee.get("s", response_model=List[EmployeeOut])
def get_employees(db: Session = Depends(db_session)) -> List[EmployeeOut]:
    return crud.Employee(db).get_employees()


@router_employee.delete("/{employee_id}")
def delete_employee(employee_id: int, db: Session = Depends(db_session)) -> None:
    return crud.Employee(db).delete_employee(employee_id)


@router_employee.put("/{employee_id}")
def put_employee(employee_id: int, employee_in: EmployeeIn, db: Session = Depends(db_session)) -> EmployeeOut:
    return crud.Employee(db).put_employee(employee_id, employee_in)
