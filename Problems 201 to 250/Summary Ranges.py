# https://leetcode.com/problems/summary-ranges

# Runtime: 48 ms, faster than 36.47% of Python3 online submissions for Summary Ranges.
# Fairly slow runtime, I think my enumerate method may be causing this to be slower.

# Memory Usage: 13.9 MB, less than 88.25% of Python3 online submissions for Summary Ranges.
# Very good memory usage, enumerate could be bloating potentially, happy with it otherwise.


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        
        start = 0
        res = []
        
        for i, num in enumerate(nums):
            
            if i+1 < len(nums) and num+1 == nums[i+1]:
                continue
                
            if start == i:
                res.append(str(num))
            else:
                res.append(str(nums[start]) + "->" + str(num))
                
               
            start = i + 1
            
            
        return res
