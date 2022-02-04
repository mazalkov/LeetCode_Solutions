# https://leetcode.com/problems/intersection-of-two-arrays

# Runtime: 58 ms, faster than 54.69% of Python3 online submissions for Intersection of Two Arrays.
# Fairly mediocre runtime, turning both lists into sets and interescting them may be causing this.

# Memory Usage: 14.1 MB, less than 90.14% of Python3 online submissions for Intersection of Two Arrays.
# Very good memory usage, nothing is declared that doesn't need to be, just creating sets.


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        return set(nums1).intersection(set(nums2))
