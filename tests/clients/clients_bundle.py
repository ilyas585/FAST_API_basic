from tests.clients.user import UserClient
from .employee import EmployeeClient
from .product import ProductClient
from .manufacturer import ManufacturerClient


class Client:
    user = UserClient()
    employee = EmployeeClient()
    product = ProductClient()
    manufacturer = ManufacturerClient()


"""
bundle-пакет
собираю в одном файле все объекты классов клиентов
"""
