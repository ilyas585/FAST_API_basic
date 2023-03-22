from tests.clients.user import UserClient
from .employee import EmployeeClient
from .product import ProductClient


class Client:
    user = UserClient()
    employee = EmployeeClient()
    product = ProductClient()


"""
bundle-пакет
собираю в одном файле все объекты классов клиентов
"""
