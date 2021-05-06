# https://leetcode.com/problems/add-binary/

# Runtime: 32 ms, faster than 72.16% of Python3 online submissions for Add Binary.
# Convert a and b to integers from binary, done on one line so may be faster

# Memory Usage: 14.2 MB, less than 80.85% of Python3 online submissions for Add Binary.
# Only a and b are declared and stored, could be why this is memory efficient


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        a, b = int(a, 2), int(b, 2)
        
        return bin(a+b)[2:]
