# https://leetcode.com/problems/reverse-bits

# Runtime: 24 ms, faster than 98.55% of Python3 online submissions for Reverse Bits.
# Very good runtime, code is not highly readable or understandable but works very quickly.

# Memory Usage: 13.8 MB, less than 98.88% of Python3 online submissions for Reverse Bits.
# Excellent memory usage, no unnecessary variables are declared, only using temporary for sum.


class Solution:
    def reverseBits(self, n: int) -> int:
        
        # not my solution, see this answer for adaptation of code:
        # https://stackoverflow.com/a/5333563/166749
        return sum(1<<(32-1-i) for i in range(32) if n>>i&1)
