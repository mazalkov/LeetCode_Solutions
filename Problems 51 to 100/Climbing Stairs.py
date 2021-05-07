# https://leetcode.com/problems/climbing-stairs/

# Runtime: 28 ms, faster than 76.28% of Python3 online submissions for Climbing Stairs.
# Uses loops, so not sure how it's so fast but oh well

# Memory Usage: 14.1 MB, less than 90.48% of Python3 online submissions for Climbing Stairs.
# Minimum number of variables, so more likely to be less space than other submissions


class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n < 3:
            return n
        
        else:
            a = 1
            b = 2

            for i in range(2, n):
                c = a + b
                a = b
                b = c

            return b
        
