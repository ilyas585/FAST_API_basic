import random
import string
import pytest


@pytest.mark.parametrize("dimension", [
    {"length": random.uniform(1, 100000),
     "width": random.uniform(1, 100000),
     "height": random.uniform(1, 100000)
     },
])
def test_positive(product_fixture, dimension):
    name = "test_" + "".join(random.sample(string.ascii_letters, 5))
    price = random.randint(0, 1000000)
    resp_post = product_fixture.api_client.product.create_product(name, price, dimension)

    product_id = resp_post.json()["id"]
    response = product_fixture.api_client.product.delete_product(product_id)

    assert response.status_code == 200, "Статус код не соответствует ожидаемому"