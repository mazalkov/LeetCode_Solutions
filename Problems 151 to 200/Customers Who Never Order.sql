-- Write your MySQL query statement below
SELECT name customers
FROM customers
WHERE id not in (
    SELECT customerid from ORDERS
)
