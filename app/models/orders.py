class Order:
    id: int
    drink_ids: list[list[int]]
    topping_ids: list[list[int]]
    total_amount: float
    discounted_amount: float

    def __init__(self,
                 id: int,
                 drink_ids: list[list[int]],
                 topping_ids: list[list[int]],
                 total_amount: float,
                 discounted_amount: float):
        self.id = id
        self.drink_ids = drink_ids
        self.topping_ids = topping_ids
        self.total_amount = total_amount
        self.discounted_amount = discounted_amount
