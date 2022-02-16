# https://leetcode.com/problems/number-complement

# Runtime: 32 ms, faster than 55.05% of Python3 online submissions for Number Complement.
# Mediocre runtime, XOR should be fast but creating the mask may be taking too much time.

# Memory Usage: 13.8 MB, less than 98.07% of Python3 online submissions for Number Complement.
# Good memory usage, creating the mask doesn't take much space, and no other variables are needed.


class Solution:
    def findComplement(self, num: int) -> int:
        
        mask = int(bin(num)[2:].replace("0","1"),2)
        
        
        return num ^ mask
