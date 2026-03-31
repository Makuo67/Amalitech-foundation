-- Missing fullname (NOT NULL violation)
INSERT INTO customers (email, phone, shipping_address)
VALUES (
        'nofullname@example.com',
        '12345',
        'Nowhere street'
    );
-- Invalid email format + duplicate email
INSERT INTO customers (fullname, email, phone, shipping_address)
VALUES (
        'John Doe',
        'not-an-email',
        '555-0000',
        '123 Fake Street'
    );
-- Duplicate unique email
INSERT INTO customers (fullname, email, phone, shipping_address)
VALUES (
        'Jane Doe',
        'not-an-email',
        '555-1111',
        'Another Street'
    );
-- Negative price (CHECK constraint violation)
INSERT INTO products (product_name, category, price)
VALUES ('Bad Product', 'Electronics', -50);
-- Missing product_name (NOT NULL violation)
INSERT INTO products (category, price)
VALUES ('Clothes', 20);
-- Non-existent product_id (FK violation)
INSERT INTO inventory (product_id, quantity_remaining)
VALUES (9999, 10);
-- Negative quantity_remaining (CHECK violation)
INSERT INTO inventory (product_id, quantity_remaining)
VALUES (1, -3);
-- Duplicate product_id (UNIQUE violation)
INSERT INTO inventory (product_id, quantity_remaining)
VALUES (1, 50);
-- Non-existent customer_id
INSERT INTO orders (customer_id, total_amount, status)
VALUES (9999, 120.50, 'Pending');
-- Negative total_amount (CHECK violation)
INSERT INTO orders (customer_id, total_amount, status)
VALUES (1, -30, 'Pending');
-- Invalid status (CHECK violation)
INSERT INTO orders (customer_id, total_amount, status)
VALUES (1, 50, 'UnknownStatus');
-- Missing status (NOT NULL violation)
INSERT INTO orders (customer_id, total_amount)
VALUES (1, 20);
-- Non-existent order_id (FK violation)
INSERT INTO order_items (order_id, product_id, quantity, purchase_price)
VALUES (9999, 1, 2, 20.00);
-- Non-existent product_id (FK violation)
INSERT INTO order_items (order_id, product_id, quantity, purchase_price)
VALUES (1, 9999, 1, 10.00);
-- Zero quantity (CHECK violation)
INSERT INTO order_items (order_id, product_id, quantity, purchase_price)
VALUES (1, 1, 0, 99.99);
-- Negative purchase price (CHECK violation)
INSERT INTO order_items (order_id, product_id, quantity, purchase_price)
VALUES (1, 1, 2, -5.00);