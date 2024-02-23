class Solution:
    def sumZero(self, n: int) -> List[int]:

        if n == 1:
            return [0]

        LIMIT = n // 2
        res = [x for x in range(-LIMIT, LIMIT+1)]

        if n % 2 == 1:
            return res

        res.remove(0)
        return res
