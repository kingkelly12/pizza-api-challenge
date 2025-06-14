# Pizza API Challenge

A RESTful API for managing pizzas and orders, built with Flask.

## Setup Steps

1. **Clone the repository:**
   ```bash
   git clone <repo-url>
   cd pizza-api-challenge
   ```

2. **Install dependencies using Pipenv:**
   ```bash
   pipenv install
   pipenv shell
   ```

3. **Set environment variables (if needed):**
   ```bash
   export FLASK_APP=server/app.py
   export FLASK_ENV=development
   ```

4. **Run the Flask server:**
   ```bash
   flask run
   ```

## Database Migration & Seeding

1. **Initialize the database (if not already):**
   ```bash
   flask db init
   ```

2. **Generate migration scripts:**
   ```bash
   flask db migrate -m "Initial migration."
   ```

3. **Apply migrations:**
   ```bash
   flask db upgrade
   ```

4. **Seed the database:**
   ```bash
   python server/seed.py
   ```

## Route Summary

| Method | Endpoint           | Description                |
|--------|--------------------|----------------------------|
| GET    | /pizzas            | List all pizzas            |
| POST   | /pizzas            | Create a new pizza         |
| GET    | /pizzas/<id>       | Get pizza by ID            |
| PUT    | /pizzas/<id>       | Update pizza by ID         |
| DELETE | /pizzas/<id>       | Delete pizza by ID         |
| GET    | /orders            | List all orders            |
| POST   | /orders            | Create a new order         |
| GET    | /orders/<id>       | Get order by ID            |

## Example Requests & Responses

### List all pizzas

**Request:**
```bash
GET /pizzas
```
**Response:**
```json
[
  {
    "id": 1,
    "name": "Margherita",
    "ingredients": "Tomato, Mozzarella, Basil",
    "price": 10.99
  }
]
```

### Create a new pizza

**Request:**
```bash
POST /pizzas
Content-Type: application/json

{
  "name": "Pepperoni",
  "ingredients": "Tomato, Mozzarella, Pepperoni",
  "price": 12.99
}
```
**Response:**
```json
{
  "id": 2,
  "name": "Pepperoni",
  "ingredients": "Tomato, Mozzarella, Pepperoni",
  "price": 12.99
}
```

### Get pizza by ID

**Request:**
```bash
GET /pizzas/1
```
**Response:**
```json
{
  "id": 1,
  "name": "Margherita",
  "ingredients": "Tomato, Mozzarella, Basil",
  "price": 10.99
}
```

### Create a new order

**Request:**
```bash
POST /orders
Content-Type: application/json

{
  "pizza_id": 1,
  "quantity": 2,
  "customer_name": "Alice"
}
```
**Response:**
```json
{
  "id": 1,
  "pizza_id": 1,
  "quantity": 2,
  "customer_name": "Alice",
  "total_price": 21.98
}
```

## Validation Rules

- **Pizza**
  - `name`: required, string, unique
  - `ingredients`: required, string
  - `price`: required, float, > 0

- **Order**
  - `pizza_id`: required, integer, must exist in pizzas
  - `quantity`: required, integer, > 0
  - `customer_name`: required, string

## Postman Usage Instructions

1. Import the API endpoints into Postman.
2. Set the base URL to `http://localhost:5000`.
3. Use the example requests above to test each endpoint.
4. For POST/PUT requests, set the body to `raw` and select `JSON`.
5. Check responses and validation errors