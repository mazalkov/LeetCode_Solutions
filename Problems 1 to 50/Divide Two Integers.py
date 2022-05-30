# https://leetcode.com/problems/divide-two-integers

# Runtime: 54 ms, faster than 31.85% of Python3 online submissions for Divide Two Integers.
# Poor runtime, my method isn't efficient despite doing bit manipulation, need to look further.

# Memory Usage: 13.9 MB, less than 76.13% of Python3 online submissions for Divide Two Integers.
# Good memory usage, a few intermediate variables are necessary to be defined for storing between loops.


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # thanks to: https://youtu.be/htX69j1jf5U
        
        if (dividend == -2147483648) and (divisor == -1):
            return 2147483647
        
        a = abs(dividend)
        b = abs(divisor)
        res = 0
        
        while (a - b) >= 0:
            
            x = 0
            
            while a - ((b << 1) << x) >= 0:
                x += 1
                
            res += 1 << x
            a -= b << x
            
    
        return -res if (dividend > 0) ^ (divisor > 0) else res
