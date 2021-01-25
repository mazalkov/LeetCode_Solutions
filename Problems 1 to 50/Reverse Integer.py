# https://leetcode.com/problems/reverse-integer/

# Runtime: 32 ms, faster than 69.81% of Python3 online submissions for Reverse Integer.
# Should run fairly fast because there's no traversing, just simple arithmetic.

# Memory Usage: 13.9 MB, less than 98.67% of Python3 online submissions for Reverse Integer.
# Tiny amount of memory usage, would come in handy if this was used in an embedded system.


class Solution:
    def reverse(self, x: int) -> int:
        
        reverse = 0
        pos = abs(x)
        
        while pos > 0:
            last_digit = pos % 10
            reverse = (reverse*10) + last_digit
            pos = pos // 10
        
        if (-2**31 <= reverse <= 2**31 - 1):
            return -1*reverse if x<0 else reverse
        else:
            return 0
