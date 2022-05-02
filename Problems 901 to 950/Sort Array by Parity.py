# https://leetcode.com/problems/sort-array-by-parity

# Runtime: 71 ms, faster than 99.07% of Python3 online submissions for Sort Array By Parity.
# Excellent runtime, preallocating the list and then 'refilling' it with values seems to be efficient.

# Memory Usage: 14.7 MB, less than 63.70% of Python3 online submissions for Sort Array By Parity.
# Good memory usage, this probably could have been done in-place without pointers, but this is more readable.


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        
        length = len(nums)
        left, right = 0, length-1
        res = [0]*length
        
        for n in nums:
            if n % 2:
                res[right] = n
                right -= 1
            else:
                res[left] = n
                left += 1
                
                
        return res
