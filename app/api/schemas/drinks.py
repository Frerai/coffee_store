from pydantic import BaseModel
from pydantic import Field


class DrinkBase(BaseModel):
    name: str = Field(..., description="The name of the drink.")
    price: float = Field(..., description="The price of the drink.")
    toppings: list[int] = Field([], description="List of topping IDs associated with the drink.")


class Drink(DrinkBase):
    id: int = Field(..., description="The unique identifier of the drink.")

    class Config:
        from_attributes = True


class DrinkCreate(DrinkBase):
    pass


class DrinkUpdate(DrinkBase):
    name: str = Field(None, description="The updated name of the drink.")
    price: float = Field(None, description="The updated price of the drink.")
    toppings: list[int] = Field([], description="List of updated topping IDs associated with the drink.")