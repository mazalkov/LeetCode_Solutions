# https://leetcode.com/problems/perfect-squares

# Runtime: 4118 ms, faster than 43.94% of Python3 online submissions for Perfect Squares.
# Poor runtime, this algorithm is not great but at least does not get Time Limit Exceeded.

# Memory Usage: 14 MB, less than 60.02% of Python3 online submissions for Perfect Squares.
# Average memory usage, the variables are quite verbose and unnecessary, but at least it's readable.


class Solution:
    def numSquares(self, n: int) -> int:
        
        if n < 3:
            return n
        
        result = [*range(0,n+1)]
        end = int(n ** (1/2))
        
        for i in range (2, end+1):
            s = i**2
            
            for j in range(s, n+1):
                result[j] = min(result[j], 1+result[j-s])
            
            
        return result[n]
