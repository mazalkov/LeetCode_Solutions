class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:

        res = 0

        N = len(grid[0])

        for row in grid:
            for i in range(N):
                if row == [row[i] for row in grid]:
                    res += 1


        return res
