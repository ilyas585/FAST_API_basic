import pytest


@pytest.mark.parametrize("new_name, new_price, new_dimension", [
    ("new name Product", None, None),
    (None, 10000, None),
    ("new name Product", 10000, None)
])
def test_positive(product_fixture, new_name, new_price, new_dimension):
    product_id = product_fixture.product_id

    response = product_fixture.api_client.product.update_product(product_id, new_name, new_price, new_dimension)

    resp = product_fixture.api_client.product.get_product_by_id(product_id)

    assert response.status_code == 200, "Статус код не соответствует ожидаемому"
    assert product_fixture.checkers.validate_json(response.json(), "schemas/product.json")
    if new_name is not None:
        assert resp.json()["name"] == new_name
    if new_price is not None:
        assert resp.json()["price"] == new_price
    if new_dimension is not None:
        assert resp.json()["dimension"] == new_dimension