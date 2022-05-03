# https://leetcode.com/problems/shortest-unsorted-continuous-subarray/

# Runtime: 306 ms, faster than 39.53% of Python3 online submissions for Shortest Unsorted Continuous Subarray.
# Fairly poor runtime, using a list comprehension on such a problem is clearly inefficient, in-place checks preferred?

# Memory Usage: 15.2 MB, less than 54.83% of Python3 online submissions for Shortest Unsorted Continuous Subarray.
# Okay memory usage, the list comprehension is again likely contributing to this, and the problem can be done in-place.


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        
        sorted_nums = sorted(nums)
        
        indices = [idx for idx, elem in enumerate(sorted_nums) if elem != nums[idx]]
        
        
        return (indices[-1] - indices[0] + 1) if indices else 0
