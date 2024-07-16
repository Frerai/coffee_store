import pytest

from app.api.crud_operations.order_operations import create_order
from app.api.crud_operations.order_operations import get_orders


@pytest.fixture
def setup_orders() -> None:
    create_order(drink_ids=[[1]], topping_ids=[[1]], total_amount=5.0, discounted_amount=5.0)


def test_create_order() -> None:
    """
    Test creating a new order.

    Example:
        >>> order = create_order(drink_ids=[[1, 3]], topping_ids=[[2, 1]], total_amount=16, discounted_amount=8)
        >>> assert order.total_amount == 10
        >>> assert order.discounted_amount == 8
    """
    order = create_order(drink_ids=[[2, 2]], topping_ids=[[1, 3]], total_amount=10, discounted_amount=8)
    assert order.total_amount == 10
    assert order.discounted_amount == 8


def test_get_orders(setup_orders) -> None:
    """
    Test retrieving a list of orders with pagination.

    Example:
        >>> orders = get_orders(skip=0, limit=3)
        >>> assert len(orders) == 2
        >>> assert orders[1].total_amount == 5
    """
    orders = get_orders(skip=0, limit=1)
    assert len(orders) == 1
    assert orders[0].total_amount == 10.0
