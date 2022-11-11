# https://leetcode.com/problems/remove-duplicates-from-sorted-array

# Runtime: 215 ms, faster than 35.61% of Python3 online submissions for Remove Duplicates from Sorted Array.
# Poor runtime, couldn't remember my previous solution without looking but this one is considerably slower.

# Memory Usage: 15.6 MB, less than 66.20% of Python3 online submissions for Remove Duplicates from Sorted Array.
# Average memory usage, too many temporary and in-between variables which could potentially be replaced.


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        cur, idx = 1, 1
        prev = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i] != prev:
                cur += 1
                prev = nums[i]
                nums[idx] = nums[i]
                idx += 1
                
                
        return cur
