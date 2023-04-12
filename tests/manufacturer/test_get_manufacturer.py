def test_positive(manufacturer_fixture):
    response = manufacturer_fixture.api_client.manufacturer.get_manufacturers()
    assert response.status_code == 200, "Статус код не соответствует ожидаемому"
    assert manufacturer_fixture.checkers.validate_items(response.json(), "schemas/manufacturer.json")