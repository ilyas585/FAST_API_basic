import pytest


@pytest.mark.parametrize("employee_id, exp_code", [
    ([1, 2, 3], 422),
    (None, 422),
    ({4}, 422),
    ({"5"}, 422)
])
def test_negative(employee_fixture, employee_id, exp_code):
    response = employee_fixture.api_client.employee.get_employee_by_id(employee_id)

    assert response.status_code == exp_code, "Статус код не соответствует ожидаемому"
