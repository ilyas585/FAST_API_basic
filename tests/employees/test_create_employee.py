import random
import string

from tests.clients.clients_bundle import employee_client
from tests.configuration import ROLE_ENUM


# add parametrize
# 1 case: name = "test_" + "".join(random.sample(string.ascii_letters, 5)), role=None
# 2 case: name = None role=admin
# 3 case: name = None, role=expert
# 4 case: name = None, role=seller
# 5 case: name = "test_" + "".join(random.sample(string.ascii_letters, 5)), role=random.choice(ROLE_ENUM)
def test_positive():
    # precondition - предусловие. Создание данных
    name = "test_" + "".join(random.sample(string.ascii_letters, 5))
    role = random.choice(ROLE_ENUM)

    # request execution
    response = employee_client.create_employee(name, role)

    assert response.status_code == 200, "Статус код не соответствует ожидаемому"
