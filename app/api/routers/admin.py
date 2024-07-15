import logging
from fastapi import APIRouter, HTTPException

from app.api.crud_operations.drink_operations import create_drink
from app.api.crud_operations.drink_operations import delete_drink
from app.api.crud_operations.drink_operations import get_drinks
from app.api.crud_operations.drink_operations import update_drink
from app.api.crud_operations.order_operations import ORDERS
from app.api.crud_operations.topping_operations import create_topping
from app.api.crud_operations.topping_operations import delete_topping
from app.api.crud_operations.topping_operations import get_toppings
from app.api.crud_operations.topping_operations import update_topping
from app.api.crud_operations.topping_operations import TOPPINGS
from app.api.schemas.drinks import Drink
from app.api.schemas.drinks import DrinkCreate
from app.api.schemas.drinks import DrinkUpdate
from app.api.schemas.toppings import Topping
from app.api.schemas.toppings import ToppingCreate
from app.api.schemas.toppings import ToppingUpdate

router = APIRouter()
logger = logging.getLogger(__name__)


#####################################################
#               DRINK ENDPOINTS                     #
#####################################################
@router.post("/drinks/", response_model=Drink)
def create_drink_route(drink: DrinkCreate):
    """
    Create a new drink with the provided details.

    Arguments:

        drink: DrinkCreate - An object containing the details of the drink to create.

    Example:

        name = "Espresso"
        price = 2.5
        toppings = [1, 2]

    Returns:

        The created drink with its details.
    """
    logger.info(f"Creating drink: {drink.name}")
    return create_drink(drink)


@router.get("/drinks/", response_model=list[Drink])
def read_drinks_route(skip: int = 0, limit: int = 10):
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


@router.put("/drinks/{drink_id}", response_model=Drink)
def update_drink_route(drink_id: int, drink: DrinkUpdate):
    """
    Update the details of an existing drink by its ID.

    Arguments:

        drink_id: int - The ID of the drink to update.
        drink: DrinkUpdate - An object containing the updated details of the drink.

    Returns:

        The updated drink with its details.
    """
    logger.info(f"Updating drink: {drink_id}")
    updated_drink = update_drink(drink_id, drink)
    if not updated_drink:
        raise HTTPException(status_code=404, detail="Drink not found")
    return updated_drink


@router.delete("/drinks/{drink_id}", response_model=Drink)
def delete_drink_route(drink_id: int):
    """
    Delete an existing drink by its ID.

    Arguments:

        drink_id: int - The ID of the drink to delete.

    Returns:

        The deleted drink with its details.
        """
    logger.info(f"Deleting drink with id: {drink_id}")
    deleted_drink = delete_drink(drink_id)
    if not deleted_drink:
        raise HTTPException(status_code=404, detail="Drink not found")
    return deleted_drink


#####################################################
#               TOPPING ENDPOINTS                   #
#####################################################
@router.post("/toppings/", response_model=Topping)
def create_topping_route(topping: ToppingCreate):
    """
    Create a new topping with the provided details.

    Arguments:

        topping: ToppingCreate - An object containing the details of the topping to create.

    Example:

        name = "Whipped Cream"
        price = 0.5

    Returns:

        The created topping with its details.
    """
    logger.info(f"Creating new topping: {topping.name}")
    return create_topping(name=topping.name, price=topping.price)


@router.get("/toppings/", response_model=list[Topping])
def read_toppings_route(skip: int = 0, limit: int = 10):
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


@router.put("/toppings/{topping_id}", response_model=Topping)
def update_topping_route(topping_id: int, topping: ToppingUpdate):
    """
    Update the details of an existing topping by its ID.

    Arguments:

        topping_id: int - The ID of the topping to update.
        topping: ToppingUpdate - An object containing the updated details of the topping.

    Returns:

        The updated topping with its details.
    """
    logger.info(f"Updating topping: {topping_id}")
    updated_topping = update_topping(topping_id, name=topping.name, price=topping.price)
    if not updated_topping:
        raise HTTPException(status_code=404, detail="Topping not found")
    return updated_topping


@router.delete("/toppings/{topping_id}", response_model=Topping)
def delete_topping_route(topping_id: int):
    """
    Delete an existing topping by its ID.

    Arguments:

        topping_id: int - The ID of the topping to delete.

    Returns:

        The deleted topping with its details.
    """
    logger.info(f"Deleting topping with id: {topping_id}")
    deleted_topping = delete_topping(topping_id=topping_id)
    if deleted_topping is None:
        logger.error(f"Topping with id {topping_id} not found")
        raise HTTPException(status_code=404, detail="Topping not found")
    return deleted_topping


@router.get("/most-used-toppings/", response_model=list[Topping])
def calculate_most_used_toppings_route():
    """
    Calculate and fetch a list of the most used toppings based on orders.

    Returns:

        A list of the most used toppings.
    """
    logger.info("Fetching most used toppings")
    topping_usage = {}

    for order in ORDERS:
        for topping_ids in order.topping_ids:
            for topping_id in topping_ids:
                if topping_id in topping_usage:
                    topping_usage[topping_id] += 1
                else:
                    topping_usage[topping_id] = 1

    most_used_topping_ids = sorted(topping_usage, key=topping_usage.get, reverse=True)
    most_used_toppings = [t for t in TOPPINGS if t.id in most_used_topping_ids]

    return most_used_toppings
