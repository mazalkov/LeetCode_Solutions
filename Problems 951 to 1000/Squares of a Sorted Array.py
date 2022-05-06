# https://leetcode.com/problems/squares-of-a-sorted-array

# Runtime: 219 ms, faster than 93.14% of Python3 online submissions for Squares of a Sorted Array.
# Excellent runtime, although I used comprehensions and built-in sort rather than manual code, it is fast.

# Memory Usage: 16.2 MB, less than 82.15% of Python3 online submissions for Squares of a Sorted Array.
# Great memory usage, Python can handle everything automatically without my definitions, so less space used.


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        return sorted([n**2 for n in nums])
