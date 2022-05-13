# https://leetcode.com/problems/merge-sorted-array

# Runtime: 32 ms, faster than 97.67% of Python3 online submissions for Merge Sorted Array.
# Brilliant runtime, iterating from the end of the list and inserting from comparison is efficient.

# Memory Usage: 13.9 MB, less than 86.49% of Python3 online submissions for Merge Sorted Array.
# Excellent memory usage, everything is done in place and only one pointer is needed for the two iterators.


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # thanks to: https://youtu.be/P1Ic85RarKY
        
        last = m + n - 1
        
        while m > 0 and n > 0:
            
            if nums1[m-1] > nums2[n-1]:
                nums1[last] = nums1[m-1]
                m -= 1
                
            else:
                nums1[last] = nums2[n-1]
                n -= 1
            
            last -= 1
            
            
        while n > 0:
            nums1[last] = nums2[n-1]
            n, last = n-1, last-1
