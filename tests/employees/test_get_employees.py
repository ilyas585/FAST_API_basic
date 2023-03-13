def test_positive(employee_fixture):
    response = employee_fixture.api_client.employee.get_employees()
    assert response.status_code == 200, "Статус код не соответствует ожидаемому"
    assert employee_fixture.checkers.validate_items(response.json(), "schemas/employee.json")
