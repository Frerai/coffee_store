import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.api.crud_operations.order_operations import create_order
from app.api.crud_operations.drink_operations import initialize_default_drinks_on_startup
from app.api.crud_operations.topping_operations import initialize_default_toppings_on_startup


@pytest.fixture(scope="module")
def setup_fastapi_test_app():
    """
    Fixture to create a TestClient for the FastAPI app.
    """
    with TestClient(app) as client:
        yield client


@pytest.fixture(scope="module", autouse=True)
def setup_default_drinks_and_toppings_data():
    """
    Fixture to initialize default drinks and toppings before running tests.
    """
    initialize_default_drinks_on_startup()
    initialize_default_toppings_on_startup()


@pytest.fixture
def setup_drinks():
    """
    Fixture to initialize default drinks for running tests on drink operations.
    """
    initialize_default_drinks_on_startup()


@pytest.fixture
def setup_orders() -> None:
    """
    Fixture to create a drink for running tests on order operations.
    """
    create_order(drink_ids=[[1]], topping_ids=[[1]], total_amount=5.0, discounted_amount=5.0)


@pytest.fixture
def setup_toppings():
    """
    Fixture to initialize default toppings for running tests on topping operations.
    """
    initialize_default_toppings_on_startup()