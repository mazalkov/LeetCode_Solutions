# https://leetcode.com/problems/search-insert-position

# Runtime: 52 ms, faster than 60.57% of Python3 online submissions for Search Insert Position.
# Decent runtime but has a lot of variation, need to consider iterative vs recursive binary search trade-offs.

# Memory Usage: 15 MB, less than 81.63% of Python3 online submissions for Search Insert Position.
# Not much memory required to just hold values of pointers and iterate over array in-place.


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        left_ptr = 0
        right_ptr = len(nums)-1
        
        # simple iterative binary search
        while left_ptr <= right_ptr:
            mid = (left_ptr + right_ptr) // 2
            
            if nums[mid] == target:
                return mid
            
            elif nums[mid] < target:
                left_ptr = mid + 1
                
            else:
                right_ptr = mid - 1
                
                
        # if we haven't found the value from above
        # return the final position of the left pointer
        # as this is where the target would be inserted
        return left_ptr
