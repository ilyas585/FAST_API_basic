def test_positive(product_fixture):
    product_id = product_fixture.product_id

    response = product_fixture.api_client.product.get_product_by_id(product_id)
    assert response.status_code == 200, "Статус код не соответствует ожидаемому"
    assert product_fixture.checkers.validate_json(response.json(), "schemas/product.json")