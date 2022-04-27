# https://leetcode.com/problems/peak-index-in-a-mountain-array

# Runtime: 89 ms, faster than 64.95% of Python3 online submissions for Peak Index in a Mountain Array.
# Good runtime, not as fast as a binary search, but just finds the max index as the array is guaranteed to be a mountain array.

# Memory Usage: 15.2 MB, less than 92.04% of Python3 online submissions for Peak Index in a Mountain Array.
# Excellent memory usage, no need to declare or store pointers, just the max function being called.


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        
        # kind of a shortcut, should use binary search instead
        return arr.index(max(arr))
