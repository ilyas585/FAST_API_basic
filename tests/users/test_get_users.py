from tests.clients.clients_bundle import user_client


def test_positive():
    response = user_client.get_users()
    assert response.status_code == 200

