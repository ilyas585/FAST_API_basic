import pytest


@pytest.mark.parametrize("name, role, exp_code", [
    ([1, 2, 3], "admin", 422),
    ("Ivan", "student", 422),
    ("Ivan", [1, 2, 3], 422),
    ("Ivan", 123, 422)
])
def test_negative(application, name, role, exp_code):
    response = application.api_client.employee.create_employee(name, role)

    assert response.status_code == exp_code, "Статус код не соответствует ожидаемому"
