import random
import string

from tests.configuration import ACCESSED_CATALOG_ENUM


def test_positive(user_fixture):
    # precondition - предусловие. Создание данных
    username = "test_" + "".join(random.sample(string.ascii_letters, 5))
    age = random.randint(0, 120)
    address = "test_address"
    accessed_catalog = {
        "name": "test_" + "".join(random.sample(string.ascii_letters, 5)),
        "catalog": random.choice(ACCESSED_CATALOG_ENUM)
    }

    # request execution
    response = user_fixture.api_client.user.create_user(username, age, address, accessed_catalog)

    assert response.status_code == 200, "Статус код не соответствует ожидаемому"
