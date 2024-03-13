class Solution:
    def pivotInteger(self, n: int) -> int:
        
        summation = n*(n+1) // 2
        x = sqrt(summation)

        return int(x) if x.is_integer() else -1
