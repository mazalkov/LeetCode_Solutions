# https://leetcode.com/problems/increasing-triplet-subsequence

# Runtime: 818 ms, faster than 71.12% of Python3 online submissions for Increasing Triplet Subsequence.
# Good runtime, only needing one pass through the items with a few checks inbetween is fairly quick.

# Memory Usage: 24.6 MB, less than 80.48% of Python3 online submissions for Increasing Triplet Subsequence.
# Great memory usage, only having to store a first and second variable, as if third exists then it is true.


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # thanks to: https://medium.com/@xiaogegexiao/increasing-triplet-subsequence-problem-995471b338f1
        
        if len(nums) < 3:
            return False
        
        first = 999999999999
        second = 999999999999
        
        for n in nums:
            if n < first:
                first = n
                
            if n > first:
                second = min(n, second)
                
            if n > second:
                return True
            
            
        return False
