import random
import pytest

from tests.checkers.general import CheckerGeneral
from tests.clients.clients_bundle import employee_client


@pytest.mark.parametrize("new_name, new_role", [
    ("new name Employee", None),
    (None, "admin"),
    ("new name Employee", "admin")
])
def test_positive(new_name, new_role):
    resp = employee_client.get_employees()
    employee_ids = [employee["id"] for employee in resp.json()]
    employee_id = random.choice(employee_ids)

    response = employee_client.update_employee(employee_id, new_name, new_role)

    resp = employee_client.get_employee_by_id(employee_id)

    assert response.status_code == 200, "Статус код не соответствует ожидаемому"
    assert CheckerGeneral().validate_json(response.json(), "schemas/employee.json")
    if new_name is not None:
        assert resp.json()["name"] == new_name
    if new_role is not None:
        assert resp.json()["role"] == new_role
