from tests.checkers.general import CheckerGeneral
from tests.clients.clients_bundle import employee_client
import random


def test_positive():
    resp = employee_client.get_employees()
    employee_ids = [employee["id"] for employee in resp.json()]
    employee_id = random.choice(employee_ids)

    response = employee_client.get_employee_by_id(employee_id)
    assert response.status_code == 200, "Статус код не соответствует ожидаемому"
    assert CheckerGeneral().validate_json(response.json(), "schemas/employee.json")
