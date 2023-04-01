import os


base_path = f"{os.path.dirname(os.path.abspath(__file__))}/"
DB_URL = os.getenv("DB_URL") or f"sqlite:///{base_path}storage/basic_db.sqlite3"
print(DB_URL)
USERNAME = os.getenv("USERNAME")

