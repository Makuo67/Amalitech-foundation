SELECT * FROM customers;
SELECT * FROM products;
SELECT * FROM inventory;
SELECT * FROM orders;
SELECT * FROM order_items;

-- update customers
-- set phone = 0790801063
-- where customer_id = 1;

-- First KPI

SELECT SUM(total_amount) AS total_revenue, status
FROM orders Group BY status;


-- Top 10 Customers By Total

SELECT 
    c.fullname AS customer_name,
    SUM(o.total_amount) AS total_spent
FROM customers c
JOIN orders o 
    ON c.customer_id = o.customer_id
GROUP BY c.customer_id
ORDER BY total_spent DESC
LIMIT 10;


--- Best Selling Products
SELECT 
    p.product_name,
    SUM(oi.quantity) AS total_quantity_sold
FROM order_items oi
JOIN products p 
    ON oi.product_id = p.product_id
GROUP BY p.product_id
ORDER BY total_quantity_sold DESC
LIMIT 5;

--- Monthly Sales Trend
SELECT 
    TO_CHAR(order_date, 'YYYY-MM') AS month,
    SUM(total_amount) AS monthly_revenue
FROM orders
GROUP BY TO_CHAR(order_date, 'YYYY-MM')
ORDER BY month;

--- Sales Rank By Category
 SELECT 
 p.category, p.product_name, SUM(oi.quantity * oi.purchase_price) as total_revenue,
 RANK() OVER(
	PARTITION BY p.category
	ORDER BY SUM(oi.quantity * oi.purchase_price) DESC
 ) AS category_rank
 FROM products p 
 JOIN order_items oi ON p.product_id = oi.product_id
 GROUP BY p.category, p.product_name;

 -- Customer Order Frequency
 SELECT 
    c.fullname,
    o.order_id,
    o.order_date AS current_order_date,
    LAG(o.order_date) OVER (
        PARTITION BY c.customer_id
        ORDER BY o.order_date
    ) AS previous_order_date
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
ORDER BY c.fullname, o.order_date;


--- Cusotmer Sales Summary View
CREATE OR REPLACE VIEW CustomerSalesSummary AS
SELECT 
    c.customer_id,
    c.fullname,
    SUM(o.total_amount) AS total_spent,
    COUNT(o.order_id) AS total_orders
FROM customers c
LEFT JOIN orders o 
    ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.fullname;


-- Stored Procedure
CREATE OR REPLACE PROCEDURE ProcessNewOrder(
    IN p_customer_id INT,
    IN p_product_id INT,
    IN p_quantity INT
)
LANGUAGE plpgsql
AS $$
DECLARE
    v_stock INT;
    v_price DECIMAL(10,2);
    v_order_id INT;
BEGIN
    -- Start transaction automatically inside procedure

    -- 1. Check inventory
    SELECT quantity_remaining INTO v_stock
    FROM inventory
    WHERE product_id = p_product_id;

    IF v_stock IS NULL THEN
        RAISE EXCEPTION 'Product does not exist in inventory.';
    END IF;

    IF v_stock < p_quantity THEN
        RAISE EXCEPTION 'Insufficient stock: available %, requested %', v_stock, p_quantity;
    END IF;

    -- 2. Reduce stock
    UPDATE inventory
    SET quantity_remaining = quantity_remaining - p_quantity
    WHERE product_id = p_product_id;

    -- 3. Get product price
    SELECT price INTO v_price
    FROM products
    WHERE product_id = p_product_id;

    -- 4. Create new order
    INSERT INTO orders (customer_id, order_date, total_amount, status)
    VALUES (p_customer_id, NOW(), (v_price * p_quantity), 'Pending')
    RETURNING order_id INTO v_order_id;

    -- 5. Create order_item
    INSERT INTO order_items (order_id, product_id, quantity, purchase_price)
    VALUES (v_order_id, p_product_id, p_quantity, v_price);

    RAISE NOTICE 'Order % created successfully.', v_order_id;

END $$;

CALL ProcessNewOrder(1, 3, 2);