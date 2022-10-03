-- https://leetcode.com/problems/combine-two-tables

-- Runtime: 784 ms, faster than 13.40% of MySQL online submissions for Combine Two Tables.
-- Poor runtime, there are likely much faster ways but I would need to look into SQL more

-- Memory Usage: 0B, less than 100.00% of MySQL online submissions for Combine Two Tables.
-- Excellent memory usage, although the 0B implies there are still potential improvements


# Write your MySQL query statement below

SELECT firstName, lastName, city, state 
FROM Person
LEFT JOIN Address
ON Person.personId = Address.PersonId
