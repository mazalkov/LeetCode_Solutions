# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted

# Runtime: 139 ms, faster than 80.40% of Python3 online submissions for Two Sum II - Input Array Is Sorted.
# Good runtime, this is less than the other version due to Leetcode's test checking, but the algorithm is better.

# Memory Usage: 14.9 MB, less than 89.05% of Python3 online submissions for Two Sum II - Input Array Is Sorted.
# Excellent memory usage, only storing two pointers allows for constant space, rather than a hash set like last time.


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # thanks to: https://youtu.be/cQ1Oz4ckceM
        
        left, right = 0, len(numbers)-1
        
        while numbers[left] + numbers[right] != target:
            
            if numbers[left] + numbers[right] < target:
                left += 1
                
            else:
                right -= 1
                
                
        return [left+1, right+1]
