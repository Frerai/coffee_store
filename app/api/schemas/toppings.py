from pydantic import BaseModel
from pydantic import Field


class ToppingBase(BaseModel):
    name: str = Field(
        ...,
        description="The name of the topping."
    )
    price: float = Field(
        ...,
        description="The price of the topping."
    )


class Topping(ToppingBase):
    id: int = Field(
        ...,
        description="The unique identifier of the topping."
    )

    class Config:
        from_attributes = True


class ToppingCreate(ToppingBase):
    pass


class ToppingUpdate(BaseModel):
    name: str | None = Field(
        None,
        description="The new name of the topping. If not provided, the current name will remain unchanged."
    )
    price: float | None = Field(
        None,
        description="The new price of the topping. If not provided, the current price will remain unchanged."
    )