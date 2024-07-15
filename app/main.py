import logging
import sys

from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from app.api.crud_operations.drink_operations import initialize_default_drinks_on_startup
from app.api.crud_operations.topping_operations import initialize_default_toppings_on_startup
from app.api.routers import admin
from app.api.routers import customer


# Setup logging.
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
stream_handler = logging.StreamHandler(sys.stdout)
log_formatter = logging.Formatter(
    "%(asctime)s [%(processName)s: %(process)d] [%(threadName)s: %(thread)d] [%(levelname)s] %(name)s: %(message)s"
)
stream_handler.setFormatter(log_formatter)
logger.addHandler(stream_handler)

# Start FastAPI App
app = FastAPI(title="coffee_store")

# Initializing default beverages and toppings.
logger.info("Loading in default data on application startup.")
initialize_default_drinks_on_startup()
initialize_default_toppings_on_startup()


# Ensure first page user will see, is the "/docs" endpoint for help.
@app.get("/", include_in_schema=False)
def root():
    return RedirectResponse(url="/docs")


app.include_router(customer.router, prefix="/customer", tags=["customer"])
app.include_router(admin.router, prefix="/admin", tags=["admin"])
