from typing import Optional, List, Type
from sqlalchemy.orm import Session

from db.models import Employee
from api.employee.schemas import Role


def get_employee_by_id(db_session: Session, employee_id: int) -> Optional[Employee]:  # Product | None
    return db_session.query(Employee).filter_by(id=employee_id).first()


def get_employees_by_name(db_session: Session, employee_name: str) -> list[Type[Employee]]:
    return db_session.query(Employee).filter_by(name=employee_name).all()


def get_all_employees(db_session: Session) -> list[Type[Employee]]:
    employees = db_session.query(Employee).all()
    return employees


def create_employee(db_session: Session, name: str, role: Role) -> Employee:
    employee = Employee(name=name, role=role)
    db_session.add(employee)  # CREATE
    db_session.commit()
    db_session.refresh(employee)  # refresh, add id to user
    return employee


def update_employee(db_session: Session, employee_id: int, new_employee):
    old_emp = get_employee_by_id(db_session, employee_id)  # UPDATE
    if old_emp is not None:
        old_emp.name = new_employee.name if new_employee.name is not None else old_emp.name
        old_emp.role = new_employee.role if new_employee.role is not None else old_emp.role
        db_session.commit()
        db_session.refresh(old_emp)
        return old_emp


def delete_employee(db_session: Session, employee_id: int) -> bool:
    employee = get_employee_by_id(db_session, employee_id)
    if employee:
        db_session.delete(employee)  # DELETE
        db_session.commit()
        return True
    else:
        return False
