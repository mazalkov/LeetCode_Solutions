# https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation

# Runtime: 224 ms, faster than 84.56% of Python3 online submissions for Prime Number of Set Bits in Binary Representation.
# Very good runtime, iterating over a range and checking if the count of 1s is within our prime list, won't work with higher left/right values.

# Memory Usage: 13.9 MB, less than 77.71% of Python3 online submissions for Prime Number of Set Bits in Binary Representation.
# Decent memory usage, it would likely be possible to look at the "pattern" of count of 1s as the number is incremented though.


class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        
        # log base 2 of 10^6 rounds up to 20
        # so most amount of bits present in 
        # left or right will be 20, need primes
        # only up to 20 because of the limit
        
        res = 0
        primes = [2, 3, 5, 7, 11, 13, 17, 19]
        
        for n in range(left, right+1):
            
            if bin(n).count("1") in primes:
                res += 1
                
                
        return res
