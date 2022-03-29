# https://leetcode.com/problems/find-the-duplicate-number

# Runtime: 596 ms, faster than 99.22% of Python3 online submissions for Find the Duplicate Number.
# Blazingly fast runtime, this solution doesn't use only constant extra space as the trade-off though.

# Memory Usage: 30.2 MB, less than 22.19% of Python3 online submissions for Find the Duplicate Number.
# Poor memory usage because Floyd's algorithm was not used, and the set will be using unnecessary memory.


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        seen = set()
        
        for n in nums:
            
            if n in seen:
                return n
            
            else:
                seen.add(n)
