# ems/largest-number-at-least-twice-of-others

# Runtime: 32 ms, faster than 96.34% of Python3 online submissions for Largest Number At Least Twice of Others.
# Excellent runtime, only need to sort the list, find the largest and pass through array once.
# I considered traversing the list in reverse, as it makes sense to start with the next largest numbers, but this was slow.

# Memory Usage: 13.9 MB, less than 64.33% of Python3 online submissions for Largest Number At Least Twice of Others.
# Above average memory usage, some variables are not necessary to define but I kept them for the sake of readability.


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        
        nums_sorted = sorted(nums)
        largest = nums_sorted[-1]
        
        for num in nums_sorted[:-1]:
            if largest < 2*num:
                return -1
            
            
        return nums.index(largest)
