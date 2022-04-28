# https://leetcode.com/problems/height-checker

# Runtime: 43 ms, faster than 67.99% of Python3 online submissions for Height Checker.
# Good runtime, doing a list comprehension on zipped lists and summing is likely not very fast.

# Memory Usage: 13.8 MB, less than 56.71% of Python3 online submissions for Height Checker.
# Okay memory usage, comprehending the zipped list is likely causing a lot of extraneous memory usage.


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        # thanks to: https://donic0211.medium.com/leetcode-1051-height-checker-514696bcd5d0
        
        sorted_heights = sorted(heights)
        
        
        return sum(h != sorted_h for h, sorted_h in zip(sorted_heights, heights))
