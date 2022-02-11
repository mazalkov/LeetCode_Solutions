# https://leetcode.com/problems/arranging-coins

# Runtime: 32 ms, faster than 95.91% of Python3 online submissions for Arranging Coins.
# Very fast runtime, can only think of making the square root more efficient to improve speed.

# Memory Usage: 13.8 MB, less than 99.27% of Python3 online submissions for Arranging Coins.
# Excellent memory usage, I think using int() instead of round() could perhaps be driving this.


class Solution:
    def arrangeCoins(self, n: int) -> int:
        
        # inelegant but works using solved
        # sum of natural numbers formula
        return int((((8*n+1)**0.5)-1) // 2)
