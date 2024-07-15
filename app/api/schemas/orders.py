from pydantic import BaseModel
from pydantic import Field


class OrderBase(BaseModel):
    drink_ids: list[list[int]] = Field(
        ...,
        description="A list of lists containing the IDs of the drinks in the order. Each inner list represents a set of"
                    " drinks to be included together."
    )
    topping_ids: list[list[int]] = Field(
        ...,
        description="A list of lists containing the IDs of the toppings in the order. Each inner list corresponds to "
                    "the toppings for the drinks in the corresponding inner list of drink_ids."
    )


class Order(OrderBase):
    id: int = Field(
        ...,
        description="The unique identifier of the order."
    )
    total_amount: float = Field(
        ...,
        description="The total amount for the order before any discounts are applied."
    )
    discounted_amount: float = Field(
        ...,
        description="The final amount for the order after applying any discounts."
    )

    class Config:
        from_attributes = True


class OrderCreate(OrderBase):
    pass
