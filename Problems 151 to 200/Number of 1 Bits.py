# https://leetcode.com/problems/number-of-1-bits

# Runtime: 44 ms, faster than 30.28% of Python3 online submissions for Number of 1 Bits.
# Likely that the binary conversion is slowing it down, perhaps not.

# Memory Usage: 14.1 MB, less than 67.59% of Python3 online submissions for Number of 1 Bits.
# The binary conversion may be storing intermediate variables, but still good memory.


class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')
