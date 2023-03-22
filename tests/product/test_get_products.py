def test_positive(product_fixture):
    response = product_fixture.api_client.product.get_products()
    assert response.status_code == 200, "Статус код не соответствует ожидаемому"
    assert product_fixture.checkers.validate_items(response.json(), "schemas/product.json")
