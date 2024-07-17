from app.models.toppings import Topping

# Create an in-memory storage for the drinks.
TOPPINGS: list[Topping] = []


def create_topping(name: str, price: float) -> Topping:
    """
    Create a new topping with the provided details.

    Args:

        name (str): The name of the topping.
        price (float): The price of the topping.

    Returns:

        Topping: The newly created topping.
    """
    # Generate a new ID for the topping.
    topping_id = len(TOPPINGS) + 1
    # Create a new topping object.
    new_topping = Topping(id=topping_id, name=name, price=price)
    # Add the new topping to the in-memory storage.
    TOPPINGS.append(new_topping)

    return new_topping


def get_topping(topping_id: int) -> Topping | None:
    """
    Get a topping by its ID.

    Args:

        topping_id (int): The ID of the topping to retrieve.

    Returns:

        Topping | None: The topping if found, otherwise None.
    """
    # Searching for the toppings id - find and return the topping with the given ID.
    return next((t for t in TOPPINGS if t.id == topping_id), None)


def get_toppings(skip: int = 0, limit: int = 10) -> list[Topping]:
    """
    Get a list of toppings, with pagination.

    Args:

        skip (int): The number of toppings to skip. Default is 0.
        limit (int): The maximum number of toppings to return. Default is 10.

    Returns:

        list[Topping]: A list of toppings.
    """
    # Return a slice of the list of toppings based on skip and limit.
    return TOPPINGS[skip:skip + limit]


def delete_topping(topping_id: int) -> Topping | None:
    """
    Delete a topping by its ID.

    Args:

        topping_id (int): The ID of the topping to delete.

    Returns:

        Topping | None: The deleted topping if found, otherwise None.
    """
    # Find the topping with the given ID.
    topping = next((t for t in TOPPINGS if t.id == topping_id), None)
    # If found, remove the topping from the in-memory storage.
    if topping:
        TOPPINGS.remove(topping)
    return topping


def update_topping(topping_id: int, name: str = None, price: float = None) -> Topping | None:
    """
    Update an existing topping's details.

    Args:

        topping_id (int): The ID of the topping to update.
        name (str, optional): The new name of the topping. Defaults to None.
        price (float, optional): The new price of the topping. Defaults to None.

    Returns:

        Topping | None: The updated topping if found, otherwise None.
    """
    # Find the topping with the given ID and update its details.
    for existing_topping in TOPPINGS:
        # If the topping ID is a match.
        if existing_topping.id == topping_id:
            if name is not None:
                # Update the toppings name.
                existing_topping.name = name
            if price is not None:
                # Update the toppings price.
                existing_topping.price = price
            return existing_topping
    return None


def initialize_default_toppings_on_startup():
    """
    Initialize the default toppings on startup.
    """
    TOPPINGS.append(Topping(id=1, name="Milk", price=2))
    TOPPINGS.append(Topping(id=2, name="Hazelnut syrup", price=3))
    TOPPINGS.append(Topping(id=3, name="Chocolate sauce", price=5))
    TOPPINGS.append(Topping(id=4, name="Lemon", price=2))
