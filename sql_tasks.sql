-- 1. Top Selling Food Items
SELECT f.name, SUM(o.quantity) AS total_sold
FROM food_items f
JOIN orders o ON f.id = o.food_item_id
GROUP BY f.id, f.name
ORDER BY total_sold DESC;

-- 2. Total Revenue
SELECT SUM(total_amount) AS total_revenue
FROM orders
WHERE status <> 'Cancelled';

-- 3. Customers With More Than 3 Orders
SELECT c.name, COUNT(o.id) AS total_orders
FROM customers c
JOIN orders o ON c.id = o.customer_id
GROUP BY c.id, c.name
HAVING COUNT(o.id) > 3;

-- 4. Most Popular Restaurant
SELECT r.name, SUM(o.quantity) AS total_orders
FROM restaurants r
JOIN food_items f ON r.id = f.restaurant_id
JOIN orders o ON f.id = o.food_item_id
GROUP BY r.id, r.name
ORDER BY total_orders DESC
LIMIT 1;

-- 5. Daily Order Report
SELECT order_date,
       COUNT(*) AS total_orders,
       SUM(total_amount) AS total_revenue
FROM orders
GROUP BY order_date;

-- 6. Rank Food Items By Sales
SELECT f.name,
       SUM(o.quantity) AS total_sold,
       RANK() OVER (ORDER BY SUM(o.quantity) DESC) AS sales_rank
FROM food_items f
JOIN orders o ON f.id = o.food_item_id
GROUP BY f.id, f.name;