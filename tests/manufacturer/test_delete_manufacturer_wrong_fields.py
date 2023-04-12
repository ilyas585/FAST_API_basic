import pytest


@pytest.mark.parametrize("manufacturer_id, code_exp", [
    ("uncorrect_id", 422),
    ([999999999], 422),
    (9999999999, 404),
    (-999999, 404)
])
def test_negative(manufacturer_fixture, manufacturer_id, code_exp):
    response = manufacturer_fixture.api_client.manufacturer.delete_manufacturer(manufacturer_id)
    assert response.status_code == code_exp, "Статус код не соответствует ожидаемому"