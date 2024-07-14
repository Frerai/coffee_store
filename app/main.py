from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root() -> dict[str, str]:
    return {"message": "Hello World!"}


# Temporary endpoint for beverages.
@app.get("/drinks")
async def get_drinks() -> list[str]:
    return ["Black Coffee", "Latte", "Mocha", "Tea"]


# Temporary endpoint for toppings.
@app.get("/drinks/toppings")
async def get_toppings() -> list[str]:
    return ["Milk", "Hazelnut syrup", "Chocolate sauce", "Lemon"]


# Temporary endpoint for admin creating drinks.
@app.get("/admin/create")
async def create_drink() -> str:
    return "Created."
