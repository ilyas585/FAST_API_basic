from api.users.schemas import UserOut
from api.product.schemas import ProductOut


class Session:
    def __init__(self):
        self.db_user: dict[int, UserOut] = {}
        self.db_product: dict[int, ProductOut] = {}
        self.cache_by_token: dict[str, UserOut] = {}

        self.current_user_id = 0
        self.current_product_id = 0

    @property
    def next_user_id(self) -> int:
        self.current_user_id += 1
        return self.current_user_id

    @property
    def next_product_id(self) -> int:
        self.current_product_id += 1
        return self.current_product_id


db_session = Session()
