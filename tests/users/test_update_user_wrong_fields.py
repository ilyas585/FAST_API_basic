import pytest


@pytest.mark.parametrize("username, age, address, accessed_catalog, exp_code", [
    (["Biy", 16], 16, "Nalchik", {"name": "besmok", "catalog": "international_food"}, 422),
    ("Biy", "age_age", "Nalchik", {"name": "besmok", "catalog": "furniture"}, 422),
    ("Biy", 16, ["Nalchik"], {"name": "besmok", "catalog": "food"}, 422),
    ("Biy", 16, "Nalchik", {"name": "besmok", "catalog": "tops"}, 422),
    ("Biy", 16, "Nalchik", ["name", "besmok", "catalog", "phones"], 422),
])
def test_negative(user_fixture, username, age, address, accessed_catalog, exp_code):
    user_id = user_fixture.user_id
    response = user_fixture.api_client.user.update_user(user_id, username, age, address, accessed_catalog)

    assert response.status_code == exp_code, "Статус код не соответствует ожидаемому"
