import random
import string



def test_positive(manufacturer_fixture):
    # precondition - предусловие. Создание данных
    name = "test_" + "".join(random.sample(string.ascii_letters, 5))
    address = "test_address"
    coefficient_sale = round(random.uniform(1,100))

    # request execution
    response = manufacturer_fixture.api_client.manufacturer.create_manufacturer(name, address, coefficient_sale)

    assert response.status_code == 200, "Статус код не соответствует ожидаемому"