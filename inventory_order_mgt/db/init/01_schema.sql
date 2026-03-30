DROP TABLE IF EXISTS customers,
products,
inventory,
orders,
order_items;
--- Database  Creation
--- create database inventorydb;
------------------
-- CustomersTable
------------------
CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,
    fullname varchar(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20),
    shipping_address TEXT NOT NULL
);
------------------
-- Products Table
------------------
CREATE TABLE products (
    product_id SERIAL PRIMARY KEY,
    product_name VARCHAR(150) NOT NULL,
    category VARCHAR(50),
    price DECIMAL(10, 2) NOT NULL CHECK (price >= 0)
);
------------------
-- Inventory Table
------------------
CREATE TABLE inventory (
    inventory_id SERIAL PRIMARY KEY,
    product_id INT NOT NULL UNIQUE,
    quantity_remaining INT NOT NULL CHECK (quantity_remaining >= 0),
    FOREIGN KEY(product_id) REFERENCES products(product_id)
);
------------------
-- Orders Table
------------------
CREATE TABLE orders (
    order_id SERIAL PRIMARY KEY,
    customer_id INT NOT NULL,
    order_date TIMESTAMP NOT NULL DEFAULT NOW(),
    total_amount DECIMAL(10, 2) NOT NULL CHECK (total_amount >= 0),
    status VARCHAR(20) NOT NULL CHECK (status IN ('Pending', 'Shipped', 'Delivered')),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);
------------------
-- Order Items Table
------------------
CREATE TABLE order_items (
    order_items_id SERIAL PRIMARY KEY,
    order_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL CHECK (quantity > 0),
    purchase_price DECIMAL(10, 2) NOT NULL CHECK (purchase_price >= 0),
    FOREIGN KEY(product_id) REFERENCES products(product_id),
    FOREIGN KEY(order_id) REFERENCES orders(order_id)
);