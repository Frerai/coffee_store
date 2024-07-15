import pytest

from app.api.crud_operations.drink_operations import create_drink
from app.api.crud_operations.drink_operations import delete_drink
from app.api.crud_operations.drink_operations import get_drink
from app.api.crud_operations.drink_operations import get_drinks
from app.api.crud_operations.drink_operations import initialize_default_drinks_on_startup
from app.api.crud_operations.drink_operations import update_drink
from app.api.schemas.drinks import DrinkCreate
from app.api.schemas.drinks import DrinkUpdate


@pytest.fixture
def setup_drinks():
    initialize_default_drinks_on_startup()


def test_create_drink():
    """
    Test creating a new drink.

    Example:
        >>> drink = DrinkCreate(name="Espresso", price=3, topping_ids=[])
        >>> created_drink = create_drink(drink)
        >>> assert created_drink.name == "Espresso"
        >>> assert created_drink.price == 3
    """
    drink = DrinkCreate(name="Espresso", price=3, topping_ids=[])
    created_drink = create_drink(drink)
    assert created_drink.name == "Espresso"
    assert created_drink.price == 3


def test_update_drink(setup_drinks):
    """
    Test updating an existing drink.

    Example:
        >>> drink_update = DrinkUpdate(name="Green Tea", price=4)
        >>> updated_drink = update_drink(4, drink_update)
        >>> assert updated_drink.name == "Green Tea"
        >>> assert updated_drink.price == 4
    """
    drink_update = DrinkUpdate(name="Green Tea", price=4)
    updated_drink = update_drink(4, drink_update)
    assert updated_drink.name == "Green Tea"
    assert updated_drink.price == 4


def test_get_drink(setup_drinks):
    """
    Test retrieving a drink by its ID.

    Example:
        >>> drink = get_drink(1)
        >>> assert drink.name == "Espresso"
        >>> assert drink.price == 4
    """
    drink = get_drink(1)
    assert drink.name == "Espresso"
    assert drink.price == 3


def test_get_drinks(setup_drinks):
    """
    Test retrieving a list of drinks with pagination.

    Example:
        >>> drinks = get_drinks(skip=0, limit=2)
        >>> assert len(drinks) == 2
    """
    drinks = get_drinks(skip=0, limit=2)
    assert len(drinks) == 2


def test_delete_drink(setup_drinks):
    """
    Test deleting a drink by its ID.

    Example:
        >>> deleted_drink = delete_drink(4)
        >>> assert deleted_drink.name == "Green Tea"
    """
    deleted_drink = delete_drink(4)
    assert deleted_drink.name == "Green Tea"
    assert deleted_drink.price == 4.0
