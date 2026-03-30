# Inventory and Order Management Database

A professional PostgreSQL relational database for e-commerce inventory and order management. Designed for 3NF normalization, this system supports customer orders, product catalog, stock tracking, and advanced business analytics through views, stored procedures, and complex queries.

**Key Features:**

- Normalized schema with constraints and relationships
- Sample data for 14 customers, 15 products, 10 orders
- KPI queries: revenue analysis, top customers/products, sales trends, category rankings
- Reusable view (`CustomerSalesSummary`) and stored procedure (`ProcessNewOrder`)
- Dockerized PostgreSQL deployment with auto-initialization

## Project Structure

```
inventory_order_mgt/
├── README.md                    # This documentation
├── TODO.md                      # Task progress
├── db/
│   ├── docker-compose.yml       # PostgreSQL Docker setup
│   ├── .env.example             # Environment variables template
│   └── init/
│       ├── 01_schema.sql        # Table DDL (customers, products, inventory, orders, order_items)
│       ├── 02_data.sql          # Sample data inserts
│       └── 03_queries.sql       # KPIs, view, stored procedure
└── erd/
    └── simba-database-schema.jpg # Entity-Relationship Diagram
```

## Database Schema

**Tables:**

| Table         | Description       | Key Fields                                                                                |
| ------------- | ----------------- | ----------------------------------------------------------------------------------------- |
| `customers`   | Customer profiles | `customer_id` (PK), `fullname`, `email` (unique), `shipping_address`                      |
| `products`    | Product catalog   | `product_id` (PK), `product_name`, `category`, `price`                                    |
| `inventory`   | Stock levels      | `inventory_id` (PK), `product_id` (unique FK), `quantity_remaining`                       |
| `orders`      | Order headers     | `order_id` (PK), `customer_id` (FK), `total_amount`, `status` (Pending/Shipped/Delivered) |
| `order_items` | Order line items  | `order_items_id` (PK), `order_id`/`product_id` (FKs), `quantity`, `purchase_price`        |

**Text ERD:**

```
customers 1 ---> * orders 1 ---> * order_items * <--- 1 products <--- 1 inventory
```

Full visual ERD: `erd/simba-database-schema.jpg`

## Setup Instructions

### Prerequisites

- Docker and Docker Compose

### Step 1: Prepare Environment

1. `cd inventory_order_mgt/db`

### Step 2: Launch Database

```
docker compose up -d
```

- Auto-runs init scripts: schema → data → queries.
- Verify: `docker ps` (look for `inventory_postgres`).
- Connect: `docker exec -it inventory_postgres psql -U admin -d inventorydb` or SQLTools (host=localhost:5432).

### Step 3: Verify Setup

Run `\dt` (tables created) and `SELECT COUNT(*) FROM customers;` (expect 14 rows).

## Key Queries and Features

All in `db/init/03_queries.sql`.

### 1. Business KPIs

```sql
-- Total revenue by order status
SELECT SUM(total_amount) AS total_revenue, status
FROM orders GROUP BY status;
```

_Sample:_ Pending: $362, Shipped: $150, Delivered: $2480

### 2. Top Customers

```sql
SELECT c.fullname, SUM(o.total_amount) AS total_spent
FROM customers c JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.fullname ORDER BY total_spent DESC LIMIT 3;
```

_Sample:_ Okeke Christian ($1335), Alice Johnson ($150), etc.

### 3. Best-Selling Products

```sql
SELECT p.product_name, SUM(oi.quantity) AS total_sold
FROM products p JOIN order_items oi ON p.product_id = oi.product_id
GROUP BY p.product_id, p.product_name ORDER BY total_sold DESC LIMIT 5;
```

### 4. Category Sales Rank (Window Function)

```sql
SELECT p.category, p.product_name, SUM(oi.quantity * oi.purchase_price) AS revenue,
RANK() OVER (PARTITION BY p.category ORDER BY SUM(oi.quantity * oi.purchase_price) DESC) AS rank
FROM products p JOIN order_items oi ON p.product_id = oi.product_id
GROUP BY p.category, p.product_name;
```

## Advanced Features

### Customer Sales Summary View

```sql
SELECT * FROM CustomerSalesSummary ORDER BY total_spent DESC;
```

Provides per-customer lifetime value and order count.

### Process New Order Stored Procedure

```sql
CALL ProcessNewOrder(customer_id := 1, p_product_id := 1, p_quantity := 2);
```

- Checks/updates inventory
- Creates order + item atomically
- Raises errors for insufficient stock

## Business Value

- **Inventory Control:** Real-time stock tracking and order deduction
- **Customer Insights:** Lifetime value, frequency, top spenders
- **Product Analytics:** Sales trends, category performance, best-sellers
- **Operational Efficiency:** Reusable procs/views reduce query duplication

Suitable for small-medium e-commerce; extensible with indexes, partitioning for scale.

## Next Steps / Extensions

- Add indexes on frequent joins (e.g., customer_id, product_id)
- Implement triggers for low-stock alerts
- Add user roles/audit logs
- Integrate with ORM (e.g., SQLAlchemy/Prisma)

---

_SQL Module Project - Amalitech Foundation_
