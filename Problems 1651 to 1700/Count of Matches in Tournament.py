class Solution:
    def numberOfMatches(self, n: int) -> int:
        if n == 1:
            return 0

        elif n <= 2:
            return 1

        elif n % 2: # odd
            return ((n-1) // 2) + self.numberOfMatches((n-1)//2 + 1)

        else: # even
            return (n//2) + self.numberOfMatches(n//2)
