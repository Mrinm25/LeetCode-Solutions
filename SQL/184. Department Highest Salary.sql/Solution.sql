SELECT 
    d.name AS Department,
    e.name AS Employee,
    e.salary AS Salary
FROM Employee e
JOIN Department d
    ON d.id = e.departmentId

JOIN (
    SELECT departmentId, 
    MAX(salary) AS Salary
    FROM Employee
    GROUP BY departmentId
) max_salary

    ON e.departmentId = max_salary.departmentId
    AND e.salary = max_salary.Salary
