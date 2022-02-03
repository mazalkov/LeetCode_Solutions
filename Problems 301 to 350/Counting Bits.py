# https://leetcode.com/problems/counting-bits

# Runtime: 121 ms, faster than 49.75% of Python3 online submissions for Counting Bits.
# Good runtime, a faster implementation is possible: https://medium.com/@edward.zhou/leet-code-338-counting-bits-explained-python3-solution-cda868e37d15

# Memory Usage: 20.8 MB, less than 91.06% of Python3 online submissions for Counting Bits.
# Brilliant memory usage, no unnecessary variables are created, or data stored.


class Solution:
    def countBits(self, n: int) -> List[int]:
        
        result = []
        
        for i in range(n+1):
            result.append(bin(i).count("1"))
            
            
        return result
