# https://leetcode.com/problems/contains-duplicate-ii

# Runtime: 1062 ms, faster than 63.86% of Python3 online submissions for Contains Duplicate II.
# Good runtime, could have been faster to implement a sliding window but not clear how it would work.

# Memory Usage: 27.1 MB, less than 79.67% of Python3 online submissions for Contains Duplicate II.
# Great memory usage, storing a single dict to use in one for loop is efficient on space.


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        indices = dict()
        
        for i in range(len(nums)):
            if nums[i] in indices:
                if i - indices[nums[i]] <= k:
                    return True
                  
            indices[nums[i]] = i
