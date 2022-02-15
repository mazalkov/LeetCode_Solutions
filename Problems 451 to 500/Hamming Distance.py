# https://leetcode.com/problems/hamming-distance

# Runtime: 28 ms, faster than 91.97% of Python3 online submissions for Hamming Distance.
# Very good runtime, only doing bitwise XOR, casting to binary, then counting the 1s.

# Memory Usage: 13.9 MB, less than 90.97% of Python3 online submissions for Hamming Distance.
# Excellent memory usage, no extra variables are created, not sure how this could be improved.


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        
        # hacky solution but works
        return bin(x ^ y).count('1')
