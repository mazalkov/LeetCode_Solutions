class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        
        N = len(piles)
        res, left, right = 0, 0, N-1
        piles.sort()

        # Strategy is to take the two highest
        # remaining coins and the lowest remaining
        # coin, and repeat til all coins are gone.
        while left < right:
            res += piles[right-1]
            left += 1
            right -= 2


        return res
