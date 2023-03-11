import random
import string
import pytest

from tests.checkers.general import CheckerGeneral
from tests.clients.clients_bundle import Client
from tests.configuration import ROLE_ENUM


class Application:
    def __init__(self):
        self.employee_id = None
        self.checkers = CheckerGeneral()
        self.api_client = Client()

    def create_employee_precondition(self):
        name = "autotest_" + "".join(random.sample(string.ascii_letters, 5))
        role = random.choice(ROLE_ENUM)
        response = self.api_client.employee.create_employee(name, role)
        assert response.status_code == 200, "can't create employee"
        self.employee_id = response.json()["id"]

    def delete_employee_post_condition(self):
        self.api_client.employee.delete_employee(self.employee_id)


fixture = Application()


@pytest.fixture(scope="session")
def application():
    # before yield is precondition
    fixture.create_employee_precondition()
    # fixture.create_user_precondition()

    yield fixture
    # after yield is post_condition
    fixture.delete_employee_post_condition()
