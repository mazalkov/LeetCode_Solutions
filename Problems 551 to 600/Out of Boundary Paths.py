class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = (10 ** 9) + 7

        cache = [[[-1] * (maxMove + 1) for _ in range(n)] for _ in range(m)]

        def traverse(x, y, moves):
            if x < 0 or y < 0 or x >= m or y >= n:
                return 1
            if moves == maxMove:
                return 0
            if cache[x][y][moves] != -1:
                return cache[x][y][moves]

            total = 0
            total += traverse(x - 1, y, moves + 1)
            total += traverse(x + 1, y, moves + 1)
            total += traverse(x, y - 1, moves + 1)
            total += traverse(x, y + 1, moves + 1)

            cache[x][y][moves] = total % MOD
            return cache[x][y][moves]

        return traverse(startRow, startColumn, 0)
