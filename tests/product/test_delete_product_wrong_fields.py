import pytest


@pytest.mark.parametrize("product_id, code_exp", [
    ("uncorrect_id", 422),
    ([999999999], 422),
    (9999999999, 404),
    (-999999, 404)
])
def test_negative(product_fixture, product_id, code_exp):
    response = product_fixture.api_client.product.delete_product(product_id)
    assert response.status_code == code_exp, "Статус код не соответствует ожидаемому"