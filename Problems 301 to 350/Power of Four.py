class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False

        # sneaky arithmetic trick
        return ceil(log(n)/log(4)) == floor(log(n)/log(4))
