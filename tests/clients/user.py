import requests

from tests.configuration import url, token


class UserClient:
    def __init__(self):
        self.url = url
        self.token = token

    @staticmethod
    def print_result(response: requests.Response):
        print("REQUEST INFO")
        print("URL", response.request.url)
        print("BODY", response.request.body)

        print("RESPONSE INFO")
        print("STATUS_CODE", response.status_code)
        print("TEXT", response.text)

    def get_users(self):
        endpoint = f"{self.url}/users"
        response = requests.get(endpoint)
        self.print_result(response)
        return response

    def get_user_by_id(self, user_id: int):
        endpoint = f"{self.url}/user/{user_id}/?token={self.token}"
        response = requests.get(endpoint)
        self.print_result(response)
        return response

    def create_user(self, username, age, address, accessed_catalog):
        endpoint = f"{self.url}/user"
        req_dict = {
            "username": username,
            "age": age,
            "address": address,
            "accessed_catalog": accessed_catalog
        }

        response = requests.post(endpoint, json=req_dict)
        self.print_result(response)
        return response

    def update_user(self, user_id: int, username: str = None, age: int = None, address: str = None,
                    accessed_catalog: dict = None):
        endpoint = f"{self.url}/user/{user_id}"
        req_dict = {
            "username": username,
            "age": age,
            "address": address,
            "accessed_catalog": accessed_catalog
        }

        response = requests.put(endpoint, json=req_dict)
        self.print_result(response)
        return response

    def delete_user(self, user_id: int):
        endpoint = f"{self.url}/user/{user_id}"
        response = requests.delete(endpoint)
        self.print_result(response)
        return response