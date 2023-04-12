import pytest


@pytest.mark.parametrize("product_id, exp_code", [
    ([1, 2, 3], 422),
    (None, 422),
    ({4}, 422),
    ({"5"}, 422)
])
def test_negative(product_fixture, product_id, exp_code):
    response = product_fixture.api_client.product.get_product_by_id(product_id)

    assert response.status_code == exp_code, "Статус код не соответствует ожидаемому"