# https://leetcode.com/problems/two-sum/

# Runtime: 36 ms, faster than 99.08% of Python3 online submissions for Two Sum.
# Probably runs so fast because it's iterating through a list, no fancy structs.

# Memory Usage: 14.4 MB, less than 75.09% of Python3 online submissions for Two Sum.
# Space usage not so efficient, hash maps may be better but this is a beginner problem.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
