from app.models.drinks import Drink
from app.api.schemas.drinks import DrinkCreate
from app.api.schemas.drinks import DrinkUpdate

# Create an in-memory storage for the drinks.
DRINKS: list[Drink] = []


def create_drink(drink: DrinkCreate) -> Drink:
    """
    Create a new drink with the provided details.

    Args:

        drink (DrinkCreate): The details of the drink to create.

    Returns:

        Drink: The newly created drink.
    """
    # Generate a new ID for the drink.
    drink_id = len(DRINKS) + 1
    # Creating a "Drink" object here.
    new_drink = Drink(id=drink_id, name=drink.name, price=drink.price, toppings=drink.toppings)
    # Adding the created "Drink" to the in-memory storage.
    DRINKS.append(new_drink)

    return new_drink


def update_drink(drink_id: int, drink: DrinkUpdate) -> Drink | None:
    """
    Update an existing drink's details.

    Args:

        drink_id (int): The ID of the drink to update.
        drink (DrinkUpdate): The new details of the drink.

    Returns:

        Drink | None: The updated drink if found, otherwise None.
    """
    # Find the drink with the given ID and update its details.
    for existing_drink in DRINKS:
        # If the drinks ID matches the one provided.
        if existing_drink.id == drink_id:
            # If provided, update the drinks name, or keep the original drink name.
            existing_drink.name = drink.name or existing_drink.name
            # If provided, update the drinks price, or keep the original drink price.
            existing_drink.price = drink.price or existing_drink.price
            # If provided, update the toppings of the drink, or keep the original drink toppings.
            existing_drink.toppings = drink.toppings or existing_drink.toppings
            return existing_drink

    return None


def get_drink(drink_id: int) -> Drink | None:
    """
    Get a drink by its ID.

    Args:

        drink_id (int): The ID of the drink to retrieve.

    Returns:

        Drink | None: The drink if found, otherwise None.
    """
    # Searching for the drinks id - find and return the drink with the given ID.
    return next((d for d in DRINKS if d.id == drink_id), None)


def get_drinks(skip: int = 0, limit: int = 10) -> list[Drink]:
    """
    Get a list of drinks, with pagination.

    Args:

        skip (int): The number of drinks to skip. Default is 0.
        limit (int): The maximum number of drinks to return. Default is 10.

    Returns:

        list[Drink]: A list of drinks.
    """
    # Return a slice of the list of drinks based on skip and limit.
    return DRINKS[skip:skip + limit]


def delete_drink(drink_id: int) -> Drink | None:
    """
    Delete a drink by its ID.

    Args:

        drink_id (int): The ID of the drink to delete.

    Returns:

        Drink | None: The deleted drink if found, otherwise None.
    """
    # Find the drink with the given ID.
    drink = get_drink(drink_id)
    # If found, remove the drink from the list.
    if drink:
        DRINKS.remove(drink)

    return drink


def initialize_default_drinks_on_startup():
    """
    Initialize the default drinks on startup.
    """
    DRINKS.append(Drink(id=1, name="Black Coffee", price=4, toppings=[]))
    DRINKS.append(Drink(id=2, name="Latte", price=5, toppings=[]))
    DRINKS.append(Drink(id=3, name="Mocha", price=6, toppings=[]))
    DRINKS.append(Drink(id=4, name="Tea", price=3, toppings=[]))
