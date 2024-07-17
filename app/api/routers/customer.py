import logging

from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import status

from app.api.crud_operations.drink_operations import get_drinks
from app.api.crud_operations.order_operations import create_order
from app.api.crud_operations.order_operations import get_orders
from app.api.crud_operations.drink_operations import get_drink
from app.api.crud_operations.topping_operations import get_topping
from app.api.crud_operations.topping_operations import get_toppings
from app.api.schemas.drinks import Drink
from app.api.schemas.orders import Order
from app.api.schemas.orders import OrderCreate
from app.api.schemas.toppings import Topping

router = APIRouter()
logger = logging.getLogger(__name__)


@router.get("/drinks/", response_model=list[Drink])
def fetch_all_drinks(skip: int = 0, limit: int = 10):
    """
    Fetch a list of all drinks, with optional pagination.

    Arguments:

        skip: int - The number of items to skip.
        limit: int - The maximum number of items to return.

    Returns:

        A list of drinks.
    """
    logger.info(f"Fetching drinks: skip={skip}, limit={limit}")

    return get_drinks(skip=skip, limit=limit)


@router.get("/toppings/", response_model=list[Topping])
def fetch_all_toppings(skip: int = 0, limit: int = 10):
    """
    Fetch a list of all toppings, with optional pagination.

    Arguments:

        skip: int - The number of items to skip.
        limit: int - The maximum number of items to return.

    Returns:

        A list of toppings.
    """
    logger.info(f"Fetching toppings: skip={skip}, limit={limit}")

    return get_toppings(skip=skip, limit=limit)


@router.post("/order-drinks/", response_model=Order)
def place_order(order: OrderCreate):
    """
    Place a new order with the provided drinks and toppings.

    Argument:

        order: OrderCreate - An object containing the details of the order.

    Example:

        drink_ids = [1, 2]
        toppings_ids = [4, 3]

    Returns:

          A successfully created order with id of drinks and toppings.
    """
    logger.info("Creating new order")

    # First, we validate whehter drink IDs have been entered in list of drink_ids.
    if not order.drink_ids or any(not drink_list for drink_list in order.drink_ids):
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Drink IDs cannot be empty.")

    drinks = []
    toppings = []

    # Find drinks ordered by the customer.
    for drink_list in order.drink_ids:
        drink_sublist = []
        for drink_id in drink_list:
            drink = get_drink(drink_id)
            if not drink:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Drink with id {drink_id} not found")
            drink_sublist.append(drink)
        drinks.append(drink_sublist)

    # Find toppings ordered by the customer.
    for topping_list in order.topping_ids:
        topping_sublist = []
        for topping_id in topping_list:
            topping = get_topping(topping_id)
            if not topping:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                    detail=f"Topping with id {topping_id} not found")
            topping_sublist.append(topping)
        toppings.append(topping_sublist)

    # Calculating toatal sum of customers order, with drinks and toppings.
    total_amount = sum(
        sum(drink.price for drink in drink_list) +
        sum(topping.price for topping in topping_list)
        for drink_list, topping_list in zip(drinks, toppings))

    # Calculating which kind of discount the customer is eligible for. Lowest discount will be applied.
    discount_1 = total_amount * 0.75 if total_amount > 12 else total_amount
    discount_2 = total_amount - min(
        drink.price + sum(topping.price for topping in topping_list)
        for drink, topping_list in zip(drinks, toppings)
    ) if len(drinks) >= 3 else total_amount

    discounted_amount = min(discount_1, discount_2)

    # Create an order which will display what drinks, topping, discount amount and total amount
    # the order has come to.
    new_order = create_order(
        drink_ids=order.drink_ids,
        topping_ids=order.topping_ids,
        total_amount=total_amount,
        discounted_amount=discounted_amount
    )

    return new_order


@router.get("/orders/", response_model=list[Order])
def fetch_all_orders(skip: int = 0, limit: int = 10):
    """
    Fetch a list of all orders, with optional pagination.

    Arguments:

        skip: int - The number of items to skip.
        limit: int - The maximum number of items to return.

    Returns:

        A list of orders.
    """
    logger.info(f"Fetching orders: skip={skip}, limit={limit}")

    return get_orders(skip=skip, limit=limit)
