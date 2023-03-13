import random
import string
import pytest

from tests.checkers.general import CheckerGeneral
from tests.clients.clients_bundle import Client
from tests.configuration import ROLE_ENUM
from tests.configuration import ACCESSED_CATALOG_ENUM


class Application:
    def __init__(self):
        self.employee_id = None
        self.user_id = None
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

    def create_user_precondition(self):
        username = "autotest_" + "".join(random.sample(string.ascii_letters, 5))
        age = random.randint(0, 120)
        address = "autotest_address"
        accessed_catalog = {"name": "autotest_" + "".join(random.sample(string.ascii_letters, 5)),
                            "catalog": random.choice(ACCESSED_CATALOG_ENUM)}
        response = self.api_client.user.create_user(username, age, address, accessed_catalog)
        assert response.status_code == 200, "can't create user"
        self.user_id = response.json()["id"]

    def delete_user_post_condition(self):
        self.api_client.user.delete_user(self.user_id)


fixture = Application()


@pytest.fixture(scope="session")
def employee_fixture():
    # before yield is precondition
    fixture.create_employee_precondition()
    yield fixture
    # after yield is post_condition
    fixture.delete_employee_post_condition()


@pytest.fixture(scope="session")
def user_fixture():
    fixture.create_user_precondition()
    yield fixture
    fixture.delete_user_post_condition()
