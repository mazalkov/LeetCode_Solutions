# https://leetcode.com/problems/add-digits/

# Runtime: 28 ms, faster than 92.88% of Python3 online submissions for Add Digits.
# Very fast runtime considering a recursive solution using list comprehension.

# Memory Usage: 13.8 MB, less than 99.73% of Python3 online submissions for Add Digits.
# Only one intermediate result, could potentially use pure arithmetic but this is efficient.


class Solution:
    def addDigits(self, num: int) -> int:
        
        result = sum(int(digit) for digit in str(num))
        
        if result < 10:
            return result
            
        else:
            return Solution.addDigits(self, result)
