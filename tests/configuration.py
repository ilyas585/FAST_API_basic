import os

mode = "docker"
url = "http://192.168.99.100" if mode == "docker" else "http://127.0.0.1"
token = ""
base_path = f"{os.path.dirname(os.path.abspath(__file__))}/"


ACCESSED_CATALOG_ENUM = ["food", "phones", "furniture", "vehicle", "international_food"]
ROLE_ENUM = ["admin", "seller", "expert"]

