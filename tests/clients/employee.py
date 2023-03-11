import requests

from tests.configuration import url, token


class EmployeeClient:
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

    def get_employees(self):
        endpoint = f"{self.url}/employees"
        response = requests.get(endpoint)
        self.print_result(response)
        return response

    def get_employee_by_id(self, employee_id: int):
        endpoint = f"{self.url}/employee/{employee_id}"
        response = requests.get(endpoint)
        self.print_result(response)
        return response

    def create_employee(self, name, role):
        endpoint = f"{self.url}/employee"
        req_dict = {
            "name": name,
            "role": role
        }

        response = requests.post(endpoint, json=req_dict)
        self.print_result(response)
        return response

    def update_employee(self, employee_id: int, name: str = None, role: str = None):
        endpoint = f"{self.url}/employee/{employee_id}"
        req_dict = {
            "name": name,
            "role": role
        }

        response = requests.put(endpoint, json=req_dict)
        self.print_result(response)
        return response

    def delete_employee(self, employee_id: int):
        endpoint = f"{self.url}/employee/{employee_id}"
        response = requests.delete(endpoint)
        self.print_result(response)
        return response
