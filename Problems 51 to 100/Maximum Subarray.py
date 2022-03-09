# https://leetcode.com/problems/maximum-subarray

# Runtime: 796 ms, faster than 77.36% of Python3 online submissions for Maximum Subarray.
# Good runtime, sliding window seems to work fairly quickly, while loop inside while loop may be slow.

# Memory Usage: 27.9 MB, less than 87.22% of Python3 online submissions for Maximum Subarray.
# Great memory usage, only defining window pointers, window sum and a largest found quantity.


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        i, j = 0, 0
        
        largest = -9999999
        w_sum = 0
        
        while j < len(nums):
            w_sum += nums[j]
            j += 1
            
            largest = max(largest, w_sum)
            
            while i<j and w_sum < 0:
                w_sum -= nums[i]
                i += 1
                
                
        return largest
