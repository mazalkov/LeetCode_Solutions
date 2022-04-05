# https://leetcode.com/problems/maximum-product-of-three-numbers

# Runtime: 264 ms, faster than 89.24% of Python3 online submissions for Maximum Product of Three Numbers.
# Excellent runtime, only performing a few calculations and taking the max value of them.

# Memory Usage: 15.1 MB, less than 97.85% of Python3 online submissions for Maximum Product of Three Numbers.
# Excellent memory usage, the array is sorted in place and no unnecessary variables are used.


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        # thanks to: https://www.geeksforgeeks.org/find-maximum-product-of-a-triplet-in-array/
        
        nums.sort()
        
        
        return max((nums[0] * nums[1] * nums[-1]), (nums[-1] * nums[-2] * nums[-3]))
