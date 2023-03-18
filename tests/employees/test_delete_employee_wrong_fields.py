import pytest


@pytest.mark.parametrize("employee_id, code_exp", [
    ("uncorrect_id", 422),
    ([999999999], 422),
    (9999999999, 404),
    (-999999, 404)
])
def test_negative(employee_fixture, employee_id, code_exp):
    response = employee_fixture.api_client.employee.delete_employee(employee_id)
    assert response.status_code == code_exp, "Статус код не соответствует ожидаемому"