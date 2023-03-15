import random
import string

import pytest

from tests.configuration import ACCESSED_CATALOG_ENUM


@pytest.mark.parametrize("username, age, address, accessed_catalog", [
    ("test_" + "".join(random.sample(string.ascii_letters, 5)), None, None, None),
    (None, random.randint(0, 120), None, None),
    (None, None, "test_address", None),
    (None, None, None, {
        "name": "test_" + "".join(random.sample(string.ascii_letters, 5)),
        "catalog": random.choice(ACCESSED_CATALOG_ENUM)
    })
])
def test_positive(user_fixture, username, age, address, accessed_catalog):
    # precondition - предусловие. Создание данных
    user_id = user_fixture.user_id

    # request execution
    response = user_fixture.api_client.user.update_user(user_id, username, age, address, accessed_catalog)

    assert response.status_code == 200, "Статус код не соответствует ожидаемому"
