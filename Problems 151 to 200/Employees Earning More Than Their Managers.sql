-- Write your MySQL query statement below
SELECT emp1.Name as Employee
FROM Employee emp1 join Employee emp2
ON emp1.ManagerId = emp2.Id
WHERE emp1.Salary > emp2.Salary
