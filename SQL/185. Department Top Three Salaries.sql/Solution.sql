-- Window Function Concept is used

SELECT Department, Employee, Salary
FROM (
    SELECT Department.name AS Department, Employee.name AS Employee, Salary,
        DENSE_RANK() 
        OVER(PARTITION BY Employee.departmentId ORDER BY salary DESC) AS 'ranking' 
    FROM Department
    JOIN Employee ON Employee.departmentId = Department.id
) AS ranked                                     -- ranked is the temporary name of this sub table
WHERE ranking <= 3

