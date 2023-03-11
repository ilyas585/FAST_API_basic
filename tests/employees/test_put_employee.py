import random
import pytest


@pytest.mark.parametrize("new_name, new_role", [
    ("new name Employee", None),
    (None, "admin"),
    ("new name Employee", "admin")
])
def test_positive(application, new_name, new_role):
    employee_id = application.employee_id

    response = application.api_client.employee.update_employee(employee_id, new_name, new_role)

    resp = application.api_client.employee.get_employee_by_id(employee_id)

    assert response.status_code == 200, "Статус код не соответствует ожидаемому"
    assert application.checkers.validate_json(response.json(), "schemas/employee.json")
    if new_name is not None:
        assert resp.json()["name"] == new_name
    if new_role is not None:
        assert resp.json()["role"] == new_role
