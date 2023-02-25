from tests.clients.clients_bundle import user_client
from tests.checkers.general import CheckerGeneral


def test_positive():
    response = user_client.get_users()
    assert response.status_code == 200, "Статус код не соответствует ожидаемому"
    assert CheckerGeneral().validate_items(response.json(), "schemas/user.json")

