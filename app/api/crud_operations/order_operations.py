from app.models.orders import Order

ORDERS: list[Order] = []
NEXT_ORDER_ID = 1


def create_order(
        drink_ids: list[list[int]], topping_ids: list[list[int]], total_amount: float,
        discounted_amount: float) -> Order:
    """
    Create a new order with the provided details.

    Args:

        drink_ids (list[list[int]]): The IDs of the drinks in the order.
        topping_ids (list[list[int]]): The IDs of the toppings in the order.
        total_amount (float): The total amount of the order.
        discounted_amount (float): The discounted amount of the order.

    Returns:

        Order: The newly created order.
    """
    global NEXT_ORDER_ID
    new_order = Order(id=NEXT_ORDER_ID, drink_ids=drink_ids, topping_ids=topping_ids, total_amount=total_amount,
                      discounted_amount=discounted_amount)
    ORDERS.append(new_order)
    NEXT_ORDER_ID += 1
    return new_order


def get_orders(skip: int = 0, limit: int = 10) -> list[Order]:
    """
    Get a list of orders, with pagination.

    Args:

        skip (int): The number of orders to skip. Default is 0.
        limit (int): The maximum number of orders to return. Default is 10.

    Returns:

        list[Order]: A list of orders.
    """
    return ORDERS[skip:skip + limit]
