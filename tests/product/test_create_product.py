import random
import string
import pytest


@pytest.mark.parametrize("dimension", [
    {"length": random.uniform(1, 100000),
     "width": random.uniform(1, 100000),
     "height": random.uniform(1, 100000)
     },
    None
])
def test_positive(product_fixture, dimension):
    # precondition - предусловие. Создание данных
    name = "test_" + "".join(random.sample(string.ascii_letters, 5))
    price = random.randint(0, 1000000)

    # request execution
    response = product_fixture.api_client.product.create_product(name, price, dimension)

    assert response.status_code == 200, "Статус код не соответствует ожидаемому"
    assert product_fixture.checkers.validate_json(response.json(), "schemas/product.json")
