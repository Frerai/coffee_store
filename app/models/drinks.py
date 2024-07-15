class Drink:
    id: int
    name: str
    price: float
    toppings: list[int] = []

    def __init__(self,
                 id: int,
                 name: str,
                 price: float,
                 toppings: list[int] = None):
        self.id = id
        self.name = name
        self.price = price
        if toppings:
            self.toppings = toppings
