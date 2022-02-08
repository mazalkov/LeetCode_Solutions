# https://leetcode.com/problems/ugly-number

# Runtime: 36 ms, faster than 67.71% of Python3 online submissions for Ugly Number.
# Fairly good runtime, doing the while loops may be inefficient but faster than sieving.

# Memory Usage: 13.8 MB, less than 99.21% of Python3 online submissions for Ugly Number.
# Very good memory usage, not defining or storing unnecessary variables, only division results.


class Solution:
    def isUgly(self, n: int) -> bool:
        
        if n <= 0:
            return False
        
        while (n % 2 == 0):
            n /= 2
            
        while (n % 3 == 0):
            n /= 3
            
        while (n % 5 == 0):
            n /= 5
            
            
        # if remainder -> ugly
        return n == 1
