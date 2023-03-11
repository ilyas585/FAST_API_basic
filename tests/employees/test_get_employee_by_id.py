def test_positive(application):
    employee_id = application.employee_id

    response = application.api_client.employee.get_employee_by_id(employee_id)
    assert response.status_code == 200, "Статус код не соответствует ожидаемому"
    assert application.checkers.validate_json(response.json(), "schemas/employee.json")
