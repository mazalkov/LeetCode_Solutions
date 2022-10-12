# https://leetcode.com/problems/largest-perimeter-triangle

# Runtime: 206 ms, faster than 91.13% of Python3 online submissions for Largest Perimeter Triangle.
# Excellent runtime, only sorting and reversing the list, then following an iterative algorithm is fast.

# Memory Usage: 15.4 MB, less than 91.63% of Python3 online submissions for Largest Perimeter Triangle.
# Excellent memory usage, array is sorted in place and no other variables are needed or used.


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        
        nums.sort()
        nums.reverse()
        
        for i in range(len(nums)-2):
            if nums[i] < nums[i+1] + nums[i+2]:
                return nums[i] + nums[i+1] + nums[i+2]
            
        return 0
        
