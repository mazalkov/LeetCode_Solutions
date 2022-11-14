# https://leetcode.com/problems/most-stones-removed-with-same-row-or-column

# Runtime: 151 ms, faster than 96.92% of Python3 online submissions for Most Stones Removed with Same Row or Column.
# Excellent runtime, an efficient algorithm which checks the union of both rows and columns for better speed.

# Memory Usage: 14.7 MB, less than 72.11% of Python3 online submissions for Most Stones Removed with Same Row or Column.
# Good memory usage, the dictionary is an efficient way of storing 'matches' and anything else is garbage collected.


class Solution:
# thanks to: https://medium.com/@thuhaochang/947-most-stones-removed-with-same-row-or-column-c52644689c8a
    def removeStones(self, stones: List[List[int]]) -> int:
        
        def search(X):
            if X != U[X]:
                U[X] = search(U[X])
            return U[X]
        
        
        def union(X, Y):
            U.setdefault(X, X)
            U.setdefault(Y, Y)
            U[search(X)] = search(Y)
            
            
        U = dict()
        
        for i, j in stones:
            union(i, ~j)
            
            
        res = len(stones)
        
        for X in U:
            if search(X) == X:
                res -= 1
                
        
        return res
