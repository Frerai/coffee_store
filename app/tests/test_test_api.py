import pytest
from fastapi.testclient import TestClient


@pytest.mark.parametrize(
    "endpoint_to_test_for, expected_status_code",
    [
        ("/customer/drinks/", 200),
        ("/customer/toppings/", 200),
        ("/customer/orders/", 200),
        ("/admin/drinks/", 200),
        ("/admin/toppings/", 200),
        ("/admin/most-used-toppings/", 200),
    ]
)
def test_get_endpoints(setup_fastapi_test_app: TestClient, endpoint_to_test_for: str, expected_status_code: int) -> None:
    """
    Test GET endpoints to ensure they return the expected status codes.
    """
    response = setup_fastapi_test_app.get(endpoint_to_test_for)
    assert response.status_code == expected_status_code


@pytest.mark.parametrize(
    "drink_input_data, expected_status_code",
    [
        ({"name": "Espresso", "price": 3.0, "toppings": []}, 200),
        ({"name": "", "price": 3.0, "toppings": []}, 422),
        ({"name": "Latte", "price": -1.0, "toppings": []}, 422),
    ]
)
def test_create_drink(setup_fastapi_test_app: TestClient, drink_input_data: dict, expected_status_code: int) -> None:
    """
    Test POST /admin/drinks/ endpoint to create a new drink.
    """
    response = setup_fastapi_test_app.post("/admin/drinks/", json=drink_input_data)
    assert response.status_code == expected_status_code


@pytest.mark.parametrize(
    "topping_input_data, expected_status_code",
    [
        ({"name": "Whipped Cream", "price": 1.5}, 200),
        ({"name": "", "price": 1.5}, 422),
        ({"name": "Honey", "price": -0.5}, 422),
    ]
)
def test_create_topping(setup_fastapi_test_app: TestClient, topping_input_data: dict, expected_status_code: int) -> None:
    """
    Test POST /admin/toppings/ endpoint to create a new topping.
    """
    response = setup_fastapi_test_app.post("/admin/toppings/", json=topping_input_data)
    assert response.status_code == expected_status_code


@pytest.mark.parametrize(
    "order_data, expected_status_code",
    [
        ({"drink_ids": [[1]], "topping_ids": [[1]]}, 200),
        ({"drink_ids": [[]], "topping_ids": [[]]}, 422),
        ({"drink_ids": [[999]], "topping_ids": [[1]]}, 404),
    ]
)
def test_create_order(setup_fastapi_test_app: TestClient, order_data: dict, expected_status_code: int) -> None:
    """
    Test POST /customer/order-drinks/ endpoint to place a new order.
    """
    response = setup_fastapi_test_app.post("/customer/order-drinks/", json=order_data)
    assert response.status_code == expected_status_code
    if expected_status_code == 200:
        order = response.json()
        assert "total_amount" in order
        assert "discounted_amount" in order
