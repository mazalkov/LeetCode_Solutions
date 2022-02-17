# https://leetcode.com/problems/max-consecutive-ones

# Runtime: 381 ms, faster than 62.94% of Python3 online submissions for Max Consecutive Ones.
# Faster than average runtine, this should be an O(n) algorithm but a faster method must exist.

# Memory Usage: 14.3 MB, less than 89.60% of Python3 online submissions for Max Consecutive Ones.
# Very good memory usage, only defining the result and a counter, not sure how to improve this.


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        res = 0
        count = 0
        
        for elem in nums:
            
            if elem:
                count += 1
                
            else:
                res = max(count, res)
                count = 0
                
        res = max(count, res)
                
            
        return res
