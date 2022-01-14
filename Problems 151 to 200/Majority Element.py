# https://leetcode.com/problems/majority-element

# Runtime: 160 ms, faster than 89.10% of Python3 online submissions for Majority Element.
# Collections is nice and fast

# Memory Usage: 15.6 MB, less than 11.23% of Python3 online submissions for Majority Element.
# Collections likely uses more memory than needed


from collections import Counter


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = Counter(nums)
        
        return c.most_common()[0][0]
