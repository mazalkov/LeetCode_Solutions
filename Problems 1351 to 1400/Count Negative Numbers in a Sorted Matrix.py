class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:

        res = 0

        for row in grid:
            res += sum(1 for x in row if x < 0)


        return res
