import pytest
from app.api.crud_operations.topping_operations import create_topping
from app.api.crud_operations.topping_operations import get_topping
from app.api.crud_operations.topping_operations import get_toppings
from app.api.crud_operations.topping_operations import delete_topping
from app.api.crud_operations.topping_operations import update_topping
from app.api.crud_operations.topping_operations import initialize_default_toppings_on_startup
from app.models.toppings import Topping


@pytest.fixture
def setup_toppings():
    initialize_default_toppings_on_startup()


def test_create_topping():
    """
    Test creating a new topping.

    Example:
        >>> topping = create_topping(name="Soya Sauce", price=19)
        >>> assert topping.name == "Soya Sauce"
        >>> assert topping.price == 19
    """
    topping = create_topping(name="Whipped Cream", price=1.5)
    assert topping.name == "Whipped Cream"
    assert topping.price == 1.5


def test_get_topping(setup_toppings):
    """
    Test retrieving a topping by its ID.

    Example:
        >>> topping = get_topping(2)
        >>> assert topping.name == "Hazelnut syrup"
        >>> assert topping.price == 3
    """
    topping = get_topping(1)
    assert topping.name == "Whipped Cream"
    assert topping.price == 1.5


def test_get_toppings(setup_toppings):
    """
    Test retrieving a list of toppings with pagination.

    Example:
        >>> toppings = get_toppings(skip=0, limit=4)
        >>> assert len(toppings) == 4
    """
    toppings = get_toppings(skip=1, limit=1)
    assert len(toppings) == 1


def test_delete_topping(setup_toppings):
    """
    Test deleting a topping by its ID.

    Example:
        >>> deleted_topping = delete_topping(4)
        >>> assert deleted_topping.name == "Lemon"
    """
    deleted_topping = delete_topping(1)
    assert deleted_topping.name == "Whipped Cream"


def test_update_topping(setup_toppings):
    """
    Test updating an existing topping.

    Example:
        >>> updated_topping = update_topping(4, name="Lime", price=125)
        >>> assert updated_topping.name == "Lime"
        >>> assert updated_topping.price == 125
    """
    updated_topping = update_topping(1, name="Soy Milk", price=2.5)
    assert updated_topping.name == "Soy Milk"
    assert updated_topping.price == 2.5
