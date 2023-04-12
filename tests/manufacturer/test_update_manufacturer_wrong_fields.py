import pytest


@pytest.mark.parametrize("name, address, coefficient_sale, exp_code", [
    ("Biy","Nalchik", 111, 422),
    (['Biy'], "Nalchik",22.2 , 422),
    ("Biy", ["Nalchik"], 22.2, 422)
])
def test_negative(manufacturer_fixture, name, address, coefficient_sale, exp_code):
    manufacturer_id = manufacturer_fixture.manufacturer_id
    response = manufacturer_fixture.api_client.manufacturer.update_manufacturer(manufacturer_fixture, name, address, coefficient_sale)

    assert response.status_code == exp_code, "Статус код не соответствует ожидаемому"