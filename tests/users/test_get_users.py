def test_positive(user_fixture):
    response = user_fixture.api_client.user.get_users()
    assert response.status_code == 200, "Статус код не соответствует ожидаемому"
    assert user_fixture.checkers.validate_items(response.json(), "schemas/user.json")
