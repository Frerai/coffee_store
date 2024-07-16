from pydantic import BaseModel
from pydantic import Field


class DrinkBase(BaseModel):
    name: str = Field(..., min_length=1, description="The name of the drink.")
    price: float = Field(..., gt=0, description="The price of the drink.")
    toppings: list[int] = Field([], description="List of topping IDs associated with the drink.")


class Drink(DrinkBase):
    id: int = Field(..., description="The unique identifier of the drink.")

    class ConfigDict:
        from_attributes = True


class DrinkCreate(DrinkBase):
    pass


class DrinkUpdate(DrinkBase):
    name: str = Field(None, min_length=1, description="The updated name of the drink.")
    price: float = Field(None, gt=0, description="The updated price of the drink.")
    toppings: list[int] = Field([], description="List of updated topping IDs associated with the drink.")