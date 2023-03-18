import pytest


@pytest.mark.parametrize("user_id, code_exp", [
    ("uncorrect_id", 422),
    ([999999999], 422),
    (9999999999, 404),
    (-999999, 404)
])
def test_negative(user_fixture, user_id, code_exp):
    response = user_fixture.api_client.user.delete_user(user_id)
    assert response.status_code == code_exp, "Статус код не соответствует ожидаемому"
