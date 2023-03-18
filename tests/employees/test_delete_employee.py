import random
import string

from tests.configuration import ROLE_ENUM


def test_positive(employee_fixture):
    name = "".join(random.sample(string.ascii_letters, 5))
    role = random.choice(ROLE_ENUM)

    resp_post = employee_fixture.api_client.employee.create_employee(name, role)

    employee_id = resp_post.json()["id"]
    response = employee_fixture.api_client.employee.delete_employee(employee_id)
    assert response.status_code == 200, "Статус код не соответствует ожидаемому"
