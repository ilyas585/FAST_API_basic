def test_positive(employee_fixture):
    employee_id = employee_fixture.employee_id

    response = employee_fixture.api_client.employee.get_employee_by_id(employee_id)
    assert response.status_code == 200, "Статус код не соответствует ожидаемому"
    assert employee_fixture.checkers.validate_json(response.json(), "schemas/employee.json")
