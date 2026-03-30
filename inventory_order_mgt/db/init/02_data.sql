-- Populating customers table
INSERT INTO customers(fullname, email, phone, shipping_address)
VALUES (
        'Okeke Christian',
        'okekemakuo2000@gmail.com',
        '0790801063',
        'KK 129, Kanombe'
    ),
    (
        'Alice Johnson',
        'alice@gmail.com',
        '0790121234',
        '123 Elm Street'
    ),
    (
        'Bob Smith',
        'bob@yahoo.com',
        '0790835678',
        '456 Pine Road'
    ),
    (
        'Charlie Brown',
        'charlie@amalitech.com',
        '0782349012',
        '789 Maple Avenue'
    ),
    (
        'David Mwangi',
        'davidmwangi@gmail.com',
        '0788123456',
        'KG 45, Kacyiru'
    ),
    (
        'Grace Uwimana',
        'graceuwimana@yahoo.com',
        '0793456789',
        'KK 210, Kicukiro'
    ),
    (
        'John Doe',
        'johndoe@gmail.com',
        '0789988776',
        'KN 12, Nyarugenge'
    ),
    (
        'Mary Njeri',
        'marynjeri@gmail.com',
        '0798765432',
        'KG 300, Gisozi'
    ),
    (
        'Samuel Okoro',
        'samuelokoro@gmail.com',
        '0787654321',
        'KK 78, Kanombe'
    ),
    (
        'Linda Brown',
        'lindabrown@yahoo.com',
        '0792345678',
        'KN 45, Remera'
    ),
    (
        'Peter Mensah',
        'petermensah@gmail.com',
        '0783456789',
        'KG 67, Kimironko'
    ),
    (
        'Esther Adebayo',
        'estheradebayo@gmail.com',
        '0794567890',
        'KK 150, Nyamirambo'
    ),
    (
        'Michael Scott',
        'michael@dundermifflin.com',
        '0785678901',
        'KN 89, Gacuriro'
    ),
    (
        'Pam Beesly',
        'pam@dundermifflin.com',
        '0796789012',
        'KG 102, Kiyovu'
    );
Populating Products table
INSERT INTO products (product_name, category, price)
VALUES ('Laptop', 'Electronics', 1200.00),
    ('Wireless Mouse', 'Electronics', 25.00),
    ('Office Chair', 'Furniture', 150.00),
    ('Water Bottle', 'Accessories', 12.00),
    ('Headphones', 'Electronics', 85.00),
    ('Smartphone', 'Electronics', 800.00),
    ('Desk Lamp', 'Furniture', 45.00),
    ('Backpack', 'Accessories', 60.00),
    ('Keyboard', 'Electronics', 30.00),
    ('Monitor', 'Electronics', 300.00),
    ('Notebook', 'Stationery', 5.00),
    ('Pen Set', 'Stationery', 10.00),
    ('Gaming Chair', 'Furniture', 250.00),
    ('USB Cable', 'Electronics', 8.00),
    ('Coffee Mug', 'Accessories', 15.00);
Populating inventory
INSERT INTO inventory (product_id, quantity_remaining)
VALUES (1, 10),
    (2, 150),
    (3, 35),
    (4, 200),
    (5, 50),
    (6, 80),
    (7, 60),
    (8, 120),
    (9, 75),
    (10, 40),
    (11, 500),
    (12, 300),
    (13, 20),
    (14, 250),
    (15, 180);
--- Populating orders
INSERT INTO orders (customer_id, order_date, total_amount, status)
VALUES (1, '2024-01-10', 1250.00, 'Delivered'),
    (2, '2024-01-12', 150.00, 'Shipped'),
    (3, '2024-01-15', 97.00, 'Pending'),
    (1, '2024-01-20', 85.00, 'Delivered'),
    (5, '2024-02-01', 800.00, 'Delivered'),
    (6, '2024-02-03', 45.00, 'Pending'),
    (7, '2024-02-05', 90.00, 'Shipped'),
    (8, '2024-02-07', 300.00, 'Delivered'),
    (9, '2024-02-10', 15.00, 'Pending'),
    (10, '2024-02-12', 250.00, 'Delivered');
-- --- order Items
INSERT INTO order_items (order_id, product_id, quantity, purchase_price)
VALUES -- Order 1 (Laptop + Mouse)
    (1, 1, 1, 1200.00),
    (1, 2, 2, 25.00),
    -- Order 2 (Office Chair)
    (2, 3, 1, 150.00),
    -- Order 3 (Water Bottle + Headphones)
    (3, 4, 1, 12.00),
    (3, 5, 1, 85.00),
    -- Order 4 (Headphones)
    (4, 5, 1, 85.00),
    (9, 15, 1, 15.00),
    -- Order 10 (Gaming Chair)
    (10, 13, 1, 250.00);