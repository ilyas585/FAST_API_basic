import random
import string

from tests.configuration import ACCESSED_CATALOG_ENUM


def test_positive(user_fixture):
    username = "test_" + "".join(random.sample(string.ascii_letters, 5))
    age = random.randint(0, 120)
    address = "test_address"
    accessed_catalog = {
        "name": "test_" + "".join(random.sample(string.ascii_letters, 5)),
        "catalog": random.choice(ACCESSED_CATALOG_ENUM)
    }
    resp_post = user_fixture.api_client.user.create_user(username, age, address, accessed_catalog)

    user_id = resp_post.json()["id"]
    response = user_fixture.api_client.user.delete_user(user_id)

    assert response.status_code == 200, "Статус код не соответствует ожидаемому"
