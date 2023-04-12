import requests

from tests.configuration import url, token

class ManufacturerClient:
    def __init__(self):
        self.url = url
        self.token = token

    @staticmethod
    def print_result(response: requests.Response):
        print("REQUEST INFO")
        print("METHOD", response.request.method)
        print("URL", response.request.url)
        print("BODY", response.request.body)

        print("RESPONSE INFO")
        print("STATUS_CODE", response.status_code)
        print("TEXT", response.text)

    def get_manufacturers(self):
        endpoint = f"{self.url}/manufacturers"
        response = requests.get(endpoint)
        self.print_result(response)
        return response

    def get_manufacturer_by_id(self, manufacturer_id: int):
        endpoint = f"{self.url}/manufacturer/{manufacturer_id}"
        response = requests.get(endpoint)
        self.print_result(response)
        return response

    def create_manufacturer(self, name, address, coefficient_sale):
        endpoint = f"{self.url}/manufacturer"
        req_dict = {
            "name": name,
            "address": address,
            "coefficient_sale": coefficient_sale
        }

        response = requests.post(endpoint, json=req_dict)
        self.print_result(response)
        return response

    def update_manufacturer(self, manufacturer_id: int, name: str = None, address: str = None, coefficient_sale:float = None):
        endpoint = f"{self.url}/manufacturer/{manufacturer_id}"
        req_dict = {
            "name": name,
            "address": address,
            "coefficient_sale": coefficient_sale
        }

        response = requests.put(endpoint, json=req_dict)
        self.print_result(response)
        return response

    def delete_manufacturer(self, manufacturer_id: int):
        endpoint = f"{self.url}/manufacturer/{manufacturer_id}"
        response = requests.delete(endpoint)
        self.print_result(response)
        return response

    def get_manufacturer_by_name(self, name: str = None):
        endpoint = f"{self.url}/manufacturer/{name}"
        response = requests.get(endpoint)
        self.print_result(response)
        return response