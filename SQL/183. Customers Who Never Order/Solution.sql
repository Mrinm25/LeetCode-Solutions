SELECT name AS Customers FROM Customers
LEFT JOIN Orders on Orders.customerId = Customers.id
WHERE customerId is NULL
