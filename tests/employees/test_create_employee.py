import random
import string
import pytest
import allure

from tests.configuration import ROLE_ENUM


@pytest.mark.parametrize("name, role", [
    ("".join(random.sample(string.ascii_letters, 5)), None),
    (None, "admin"),
    (None, "expert"),
    (None, "seller"),
    ("".join(random.sample(string.ascii_letters, 5)), random.choice(ROLE_ENUM))
])
@allure.title("[positive] create Employee")
def test_positive(employee_fixture, name, role):
    with allure.step("Выполнение запроса"):
        response = employee_fixture.api_client.employee.create_employee(name, role)

    with allure.step("Проверка результата."):
        assert response.status_code == 200, "Статус код не соответствует ожидаемому"
        assert employee_fixture.checkers.validate_json(response.json(), "schemas/employee.json")
