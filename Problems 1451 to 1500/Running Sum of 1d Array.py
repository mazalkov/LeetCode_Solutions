# https://leetcode.com/problems/running-sum-of-1d-array

# Runtime: 50 ms, faster than 65.50% of Python3 online submissions for Running Sum of 1d Array.
# Decent runtime, pre-allocating the list may allow for speed increase, but the for loop could be optimised.

# Memory Usage: 14.1 MB, less than 27.03% of Python3 online submissions for Running Sum of 1d Array.
# Poor memory usage, not sure how to improve this currently as a result list is required at some point.


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        res = [nums[0]] * len(nums)
        
        for i in range(1, len(nums)):
            res[i] = nums[i] + res[i-1]
            
            
        return res
        
