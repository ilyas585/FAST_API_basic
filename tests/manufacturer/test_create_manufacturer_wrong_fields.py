import pytest


@pytest.mark.parametrize("name, address, coefficient_sale, exp_code", [
    ("Biy","Nalchik", 'abrakadabra', 422),
    (['Biy'], "Nalchik",22.2 , 422),
    ("Biy", ["Nalchik"], 22.2, 422)
])
def test_negative(manufacturer_fixture, name, address, coefficient_sale, exp_code):
    response = manufacturer_fixture.api_client.manufacturer.create_manufacturer(name, address, coefficient_sale)

    assert response.status_code == exp_code, "Статус код не соответствует ожидаемому"