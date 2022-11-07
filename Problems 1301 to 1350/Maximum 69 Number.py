# https://leetcode.com/problems/maximum-69-number

# Runtime: 36 ms, faster than 87.86% of Python3 online submissions for Maximum 69 Number.
# Excellent runtime, bit of a hacky solution concatenating int casts of strings but it works.

# Memory Usage: 13.8 MB, less than 95.47% of Python3 online submissions for Maximum 69 Number.
# Excellent memory usage, only having to enumerate a string representation of the number.


class Solution:
    def maximum69Number (self, num: int) -> int:
        
        for i, digit in enumerate(str(num)):
            if digit == "6":
                return int(str(num)[:i] + "9" + str(num)[i+1:])
           
        return num
