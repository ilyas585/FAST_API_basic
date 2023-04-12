import pytest


@pytest.mark.parametrize("id_prd, name, price, dimension, exp_code", [
    (1,[1, 2, 3], "14.6", {14: '13', 15: '14', 16: '15'}, 422),
    ("23", "Ivan", [14.6], {"length": "14, 14, 14", "width": "14, 14, 14", "height": "14, 14, 14"}, 422),
    ([43],"Ivan", [1, 2, 3], {"len": "14, 14, 14", "wih": "14, 14, 14", "hht": "14, 14, 14"}, 422),
    ("idk","Ivan", ["16"], {"smth": 17}, 422)
])
def test_negative(product_fixture, id_prd, name, price, dimension, exp_code):
    response = product_fixture.api_client.product.update_product(id_prd, name, price, dimension)

    assert response.status_code == exp_code, "Статус код не соответствует ожидаемому"