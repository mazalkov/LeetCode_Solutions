# https://leetcode.com/problems/integer-to-roman 

# Runtime: 48 ms, faster than 96.07% of Python3 online submissions for Integer to Roman.
# Excellent runtime, this approach is not particularly human-readable but it is very fast.

# Memory Usage: 13.9 MB, less than 80.12% of Python3 online submissions for Integer to Roman..
# Great memory usage, holding a lookup is barely any overhead, and the result is dynamic.


class Solution:
    def intToRoman(self, num: int) -> str:
        
        lookup = [["I", 1], ["IV", 4], ["V", 5], ["IX", 9], ["X", 10],
                 ["XL", 40], ["L", 50], ["XC", 90], ["C", 100], ["CD", 400],
                  ["D", 500], ["CM", 900], ["M", 1000]]
        
        res = ""
        
        for sym, val in reversed(lookup):
            if num // val:
                count = num // val
                res += (sym * count)
                num = num % val
                
        return res
