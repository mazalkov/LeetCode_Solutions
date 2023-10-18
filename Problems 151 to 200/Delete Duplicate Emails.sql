-- Write your MySQL query statement below
DELETE person2
FROM Person person1 JOIN person person2
WHERE person1.email = person2.email
AND person1.id < person2.id
