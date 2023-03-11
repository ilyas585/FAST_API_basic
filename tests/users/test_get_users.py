def test_positive(application):
    response = application.api_client.user.get_users()
    assert response.status_code == 200, "Статус код не соответствует ожидаемому"
    assert application.checkers.validate_items(response.json(), "schemas/user.json")
