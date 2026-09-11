SELECT e.name as Employee FROM Employee e
JOIN Employee m
ON e.managerId = m.id
WHERE m.salary < e.salary;
