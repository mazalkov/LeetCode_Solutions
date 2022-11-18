# https://leetcode.com/problems/ugly-number

# Runtime: 38 ms, faster than 87.43% of Python3 online submissions for Ugly Number.
# Excellent runtime, seems to be an improvement over the previous with some changes.

# Memory Usage: 13.8 MB, less than 60.08% of Python3 online submissions for Ugly Number.
# Average memory usage, not sure how to improve efficiency without changing structure.


class Solution:
    def isUgly(self, n: int) -> bool:
        
        if n<=0: return False
        
        while n != 1:
            
            if not n % 2:
                n /= 2
                continue
                
            if not n % 3:
                n /= 3
                continue
                
            if not n % 5:
                n /= 5
                continue
                
            return False
        
        return True
