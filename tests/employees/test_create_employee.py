import random
import string
import pytest

from tests.configuration import ROLE_ENUM


@pytest.mark.parametrize("name, role", [
    ("".join(random.sample(string.ascii_letters, 5)), None),
    (None, "admin"),
    (None, "expert"),
    (None, "seller"),
    ("".join(random.sample(string.ascii_letters, 5)), random.choice(ROLE_ENUM))
])
def test_positive(employee_fixture, name, role):
    response = employee_fixture.api_client.employee.create_employee(name, role)

    assert response.status_code == 200, "Статус код не соответствует ожидаемому"
    assert employee_fixture.checkers.validate_json(response.json(), "schemas/employee.json")
