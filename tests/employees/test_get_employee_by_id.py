import random


def test_positive(application):
    resp = application.api_client.employee.get_employees()
    employee_ids = [employee["id"] for employee in resp.json()]
    employee_id = random.choice(employee_ids)

    response = application.api_client.employee.get_employee_by_id(employee_id)
    assert response.status_code == 200, "Статус код не соответствует ожидаемому"
    assert application.checkers.validate_json(response.json(), "schemas/employee.json")
