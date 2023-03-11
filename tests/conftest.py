import pytest

from tests.checkers.general import CheckerGeneral
from tests.clients.clients_bundle import Client


class Application:
    def __init__(self):
        self.checkers = CheckerGeneral()
        self.api_client = Client()


fixture = Application()


@pytest.fixture
def application():
    return fixture
