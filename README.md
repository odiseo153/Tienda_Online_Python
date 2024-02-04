>[NOTE]
>Disfruta de la app

# Online Store API in Python

This Python API, developed with Flask and the Peewee ORM, emulates the functionality of a basic online store. It mimics both entities and business logic commonly found in an e-commerce setting.

## Endpoints:

### Product Routes

#### Get all products
```http
GET /productos
```

#### Get product by ID
```http
GET /productos/id
```

#### Create a new product
```http
POST /productos
```

#### Delete a product
```http
DELETE /productos/id
```

#### Update a product
```http
PUT /productos/id
```

### User Routes

#### User login
```http
POST /login
```

#### Get user by ID
```http
GET /usuario/id
```

#### Get all users
```http
GET /usuario
```

#### Create a new user
```http
POST /usuario
```

#### Delete a user
```http
DELETE /usuario/id
```

#### Update a user
```http
PUT /usuario/id
```

### Order Routes

#### Get order by ID
```http
GET /pedido/id
```

#### Get all orders
```http
GET /pedido
```

#### Create a new order
```http
POST /pedido
```

#### Delete an order
```http
DELETE /pedido/id
```

#### Update an order
```http
PUT /pedido/id
```

### Shopping Cart Routes

#### Get shopping cart by ID
```http
GET /carrito/id
```

#### Get all shopping carts
```http
GET /carrito
```

#### Create a new shopping cart
```http
POST /carrito
```

#### Delete a shopping cart
```http
DELETE /carrito/id
```

#### Update a shopping cart
```http
PUT /carrito/id
```

### Order Details Routes

#### Get details of a specific order in the shopping cart by ID
```http
GET /detallecarrito/id
```

#### Get all order details in the shopping cart
```http
GET /detallecarrito
```

#### Create new order details in the shopping cart
```http
POST /detallecarrito
```

#### Delete order details in the shopping cart
```http
DELETE /detallecarrito/id
```

#### Update order details in the shopping cart
```http
PUT /detallecarrito/id
```

### Order History Routes

#### Get order history by user ID
```http
GET /historial/id
```

#### Get all order histories
```http
GET /historial
```

## Running the Application
```bash
python main.py
```

This will start the application in debug mode. **Note:** Replace `main.py` with the actual filename of your Python script. Customize routes and controllers according to your specific requirements.
