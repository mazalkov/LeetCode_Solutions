# https://leetcode.com/problems/arithmetic-slices

# Runtime: 44 ms, faster than 72.54% of Python3 online submissions for Arithmetic Slices.
# Good runtime, there may be a way to derive an equation for this, but this method is understandable.

# Memory Usage: 14.1 MB, less than 97.59% of Python3 online submissions for Arithmetic Slices.
# Excellent memory usage, iterating over the array and only storing count and result variables.


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        
        dynamic_count = 0 
        res = 0
        
        for i in range(2, len(nums)):
            
            if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
                dynamic_count += 1
                res += dynamic_count
                
            else:
                dynamic_count = 0
                
                
        return res
