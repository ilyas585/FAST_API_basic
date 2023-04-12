import random
import string



def test_positive(manufacturer_fixture):
    name = "test_" + "".join(random.sample(string.ascii_letters, 5))
    address = "test_address"
    coefficient_sale = round(random.uniform(1, 100))

    resp_post = manufacturer_fixture.api_client.manufacturer.create_manufacturer(name, address, coefficient_sale)

    manufacturer_id = resp_post.json()["id"]
    response = manufacturer_fixture.api_client.manufacturer.delete_manufacturer(manufacturer_id)

    assert response.status_code == 200, "Статус код не соответствует ожидаемому"