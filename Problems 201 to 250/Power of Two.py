# https://leetcode.com/problems/power-of-two

# Runtime: 45 ms, faster than 17.47% of Python3 online submissions for Power of Two.
# Assuming it's not fast because Python isn't used to natively manipulating bits.

# Memory Usage: 14.1 MB, less than 89.95% of Python3 online submissions for Power of Two.
# Space should be fine because no unnecessary variables are created for storing temp values.


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return (n & (n-1) == 0) and n != 0
