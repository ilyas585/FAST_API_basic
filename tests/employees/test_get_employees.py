def test_positive(application):
    response = application.api_client.employee.get_employees()
    assert response.status_code == 200, "Статус код не соответствует ожидаемому"
    assert application.checkers.validate_items(response.json(), "schemas/employee.json")
