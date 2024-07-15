# Coffee Store API

This API manages a coffee store, allowing customers to browse drinks and toppings, place orders, and admins to manage drinks and toppings inventory.

## Getting Started

To run the Coffee Store API locally, follow these steps:

### Prerequisites

- Internet access - or borrow your grandparents' (they wouldn't know anyway)
- Have a machine - or borrow your grandparents' (again, here they wouldn't know anything either)
- Docker installed on your machine
- Have some spare time to kill

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/frerai/coffee_store.git
   cd coffee_store

2. Build the Docker image: 
   ```bash
   docker build -t coffee_store .

3. Run the Docker container:
   ```bash
   docker run -p 8100:8100 coffee_store

Opening the application from your Docker logs, you should be redirected to http://localhost:8100/docs
where the API will be accessible.

## Endpoints
________________________

### Customer Endpoints

#### Fetch All Drinks

- **URL:** `/customer/drinks/`
- **Method:** `GET`
- **Description:** Fetches a list of all drinks with optional pagination.
- **Example:**
   ```bash
   curl -X 'GET' \
  'http://0.0.0.0:8100/customer/drinks/?skip=0&limit=10' \
  -H 'accept: application/json'

#### Fetch All Toppings

- **URL:** `/customer/toppings/`
- **Method:** `GET`
- **Description:** Fetches a list of all toppings with optional pagination.
- **Example:**
   ```bash
  curl -X 'GET' \
  'http://0.0.0.0:8100/customer/toppings/?skip=0&limit=10' \
  -H 'accept: application/json'

#### Place Order

- **URL:** `/customer/order-drinks/`
- **Method:** `POST`
- **Description:** Places a new order with selected drinks and toppings.
- **Example:**
   ```bash
   curl -X 'POST' \
  'http://0.0.0.0:8100/customer/order-drinks/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "drink_ids": [
    [
      3
    ]
  ],
  "topping_ids": [
    [
      2, 4
    ]
  ]
}'

#### Fetch All Orders

- **URL:** `/customer/orders/`
- **Method:** `GET`
- **Description:** Fetches a list of all orders with optional pagination.
- **Example:**
   ```bash
   curl -X 'GET' \
  'http://0.0.0.0:8100/customer/orders/?skip=0&limit=10' \
  -H 'accept: application/json'

### Admin Endpoints

#### Create Drink

- **URL:** `/admin/drinks/`
- **Method:** `POST`
- **Description:** Creates a new drink.
- **Example:**
   ```bash
   curl -X 'POST' \
  'http://0.0.0.0:8100/admin/drinks/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "Hot Goats Milk",
  "price": 550,
  "toppings": []
}'

#### Read Drinks

- **URL:** `/admin/drinks/`
- **Method:** `GET`
- **Description:** Reads all available drinks with optional pagination.
- **Example:**
   ```bash
   curl -X 'GET' \
  'http://0.0.0.0:8100/admin/drinks/?skip=0&limit=10' \
  -H 'accept: application/json'
  
#### Update Drink

- **URL:** `/admin/drinks/{drink_id}`
- **Method:** `PUT`
- **Description:** Updates an existing drink by ID.
- **Example:**
   ```bash
   curl -X 'PUT' \
  'http://0.0.0.0:8100/admin/drinks/4' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "Day old cold cappuccino"
  "price": 0.2,
  "toppings": [4]
}'

#### Delete Drink

- **URL:** `/admin/drinks/{drink_id}`
- **Method:** `DELETE`
- **Description:** Deletes an existing drink by ID.
- **Example:**
   ```bash
   curl -X 'DELETE' \
  'http://0.0.0.0:8100/admin/drinks/2' \
  -H 'accept: application/json'

#### Create Topping

- **URL:** `/admin/toppings/`
- **Method:** `POST`
- **Description:** Creates a new topping.
- **Example:**
   ```bash
   curl -X 'POST' \
  'http://0.0.0.0:8100/admin/toppings/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "Premium Gouda",
  "price": 2000
}'

#### Read Toppings

- **URL:** `/admin/toppings/`
- **Method:** `GET`
- **Description:** Reads all available toppings with optional pagination.
- **Example:**
   ```bash
   curl -X 'GET' \
  'http://0.0.0.0:8100/admin/toppings/?skip=0&limit=10' \
  -H 'accept: application/json'
  

#### Update Topping

- **URL:** `/admin/toppings/{topping_id}`
- **Method:** `PUT`
- **Description:** Updates an existing topping by ID.
- **Example:**
   ```bash
   curl -X 'PUT' \
  'http://0.0.0.0:8100/admin/toppings/4' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "Fresh Romanian Telemea",
  "price": 2001
}'

#### Delete Topping

- **URL:** `/admin/toppings/{topping_id}`
- **Method:** `DELETE`
- **Description:** Deletes an existing topping by ID.
- **Example:**
   ```bash
   curl -X 'DELETE' \
  'http://0.0.0.0:8100/admin/toppings/2' \
  -H 'accept: application/json'

#### Get most used Topping

- **URL:** `/admin/most-used-toppings/`
- **Method:** `GET`
- **Description:** Retrieves the most used Toppings by orders.
- **Example:**
   ```bash
  curl -X 'GET' \
  'http://0.0.0.0:8100/admin/most-used-toppings/' \
  -H 'accept: application/json'


## Tests
________________________

### Running tests
To run tests verbosely:
```bash
  docker run coffee_store pytest -vv
