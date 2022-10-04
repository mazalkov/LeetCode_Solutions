# https://leetcode.com/problems/duplicate-emails

# Runtime: 435 ms, faster than 52.86% of MySQL online submissions for Duplicate Emails.
# Average runtime, unsure how to improve this, need to look into SQL statements a lot more.

# Memory Usage: 0B, less than 100.00% of MySQL online submissions for Duplicate Emails.
# Must be a bug with LeetCode due to apparently being 0 bytes, memory not so important here.


# Write your MySQL query statement below

# thanks to: https://stackoverflow.com/questions/2594829/finding-duplicate-values-in-a-sql-table
SELECT email 
FROM Person
GROUP BY email
HAVING COUNT(email) > 1
