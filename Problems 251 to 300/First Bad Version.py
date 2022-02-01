# https://leetcode.com/problems/first-bad-version

# Runtime: 28 ms, faster than 87.48% of Python3 online submissions for First Bad Version.
# Binary search should be fast for large n, and Python isn't too slow to achieve this.

# Memory Usage: 13.9 MB, less than 98.30% of Python3 online submissions for First Bad Version.
# Very good memory usage, only defining 4 other variables should guarantee less space used.


# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        left = 1
        right = n
        ptr = -1
        
        while left <= right:
            mid = (left + right) // 2
            
            if isBadVersion(mid):
                ptr = mid
                right = mid - 1
                
            else:
                left = mid + 1
                
                
        return ptr
