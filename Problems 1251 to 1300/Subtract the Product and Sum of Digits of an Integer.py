# https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer

# Runtime: 51 ms, faster than 53.49% of Python3 online submissions for Subtract the Product and Sum of Digits of an Integer.
# Average runtime, this could easily be sped up with list comprehensions or something similar, but was running out of time.

# Memory Usage: 13.7 MB, less than 95.32% of Python3 online submissions for Subtract the Product and Sum of Digits of an Integer.
# Excellent memory usage, perhaps the trade-off of not using comprehensions, not storing anything other than the result variables.


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        
        prod = add = int(str(n)[0])
        
        for digit in (str(n)[1:]):
            prod *= int(digit)
            add += int(digit)
            
            
        return prod - add
