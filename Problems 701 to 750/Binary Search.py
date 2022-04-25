# https://leetcode.com/problems/binary-search

# Runtime: 264 ms, faster than 72.73% of Python3 online submissions for Binary Search.
# Fairly good runtime, an iterative approach is used to avoid multiple recursive calls.

# Memory Usage: 15.4 MB, less than 75.06% of Python3 online submissions for Binary Search.
# Fairly good memory usage, storing left and right as pointers may be better than many recursion frames.


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # thanks to: https://velog.io/@ahn16/Leetcode-704-Python-Binary-Search
        
        left, right = 0, len(nums)
        
        while left < right:
            
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
                
            elif nums[mid] > target:
                right = mid
                
            elif nums[mid] < target:
                left = mid+1
                
                
        return -1
