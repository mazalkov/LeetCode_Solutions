# https://leetcode.com/problems/fibonacci-number

# Runtime: 30 ms, faster than 86.93% of Python3 online submissions for Fibonacci Number.
# Very good runtime, calculating the Nth value directly without any need for recursion or loops.

# Memory Usage: 13.9 MB, less than 83.15% of Python3 online submissions for Fibonacci Number.
# Great memory usage, could perhaps define sqrt(5) and then use the variable, or similar for others.


from math import sqrt


class Solution:
    def fib(self, n: int) -> int:

        # messy result using direct formula
        return int((((1+sqrt(5))**n)-((1-sqrt(5)))**n)/(2**n*sqrt(5)))
