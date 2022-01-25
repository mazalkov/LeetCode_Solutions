# https://leetcode.com/problems/contains-duplicate

# Runtime: 452 ms, faster than 57.84% of Python3 online submissions for Contains Duplicate.
# Good runtime, using in-built sets should be the fastest way to do this in Python.

# Memory Usage: 26 MB, less than 38.81% of Python3 online submissions for Contains Duplicate.
# Space usage is adequate, not sure how to use less without calling set() or len() in each.


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        return len(set(nums)) != len(nums)
