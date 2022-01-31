# https://leetcode.com/problems/missing-number

# Runtime: 227 ms, faster than 31.35% of Python3 online submissions for Missing Number.
# Fairly slow runtime, not sure why summing or taking the length makes it so slow.

# Memory Usage: 15.2 MB, less than 99.03% of Python3 online submissions for Missing Number.
# Great in terms of low space usage, since nothing unnecessary is being stored.


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        correct_sum = ((len(nums)) * (len(nums)+1)) // 2
        
        return correct_sum - sum(nums)
