# https://leetcode.com/problems/set-mismatch

# Runtime: 207 ms, faster than 89.89% of Python3 online submissions for Set Mismatch.
# Good runtime, the constant checking of a set is likely not faster than alternatives.

# Memory Usage: 15.8 MB, less than 55.38% of Python3 online submissions for Set Mismatch.
# Average memory usage, lots of variables are created, and the set is also contributing to this.


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        # thanks to: https://dev.to/seanpgallivan/solution-set-mismatch-4ejh
        
        repeated = 0
        seen = set()
        N = len(nums)
        sumN = (N * (N+1)) // 2
        
        for n in nums:
            sumN -= n
            
            if n in seen:
                repeated = n
            seen.add(n)
            
            
        return [repeated, sumN + repeated]
