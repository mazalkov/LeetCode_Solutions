# https://leetcode.com/problems/shift-2d-grid

# Runtime: 172 ms, faster than 88.30% of Python3 online submissions for Shift 2D Grid.
# Excellent runtime, result is pre-allocated and speedily calculated with in the for loops.

# Memory Usage: 14.1 MB, less than 89.14% of Python3 online submissions for Shift 2D Grid.
# Excellent memort usage, only having to calculate and store new index values for shifting.


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        # could have used numpy.roll but instead used: https://youtu.be/nJYFh4Dl-as
        
        rows, cols = len(grid), len(grid[0])
        
        res = [[0] * cols for i in range(rows)]
        
        for r in range(rows):
            for c in range(cols):
                
                newPos = (r * cols + c + k) % (rows * cols)
                new_r, new_c = [newPos // cols, newPos % cols]
                
                res[new_r][new_c] = grid[r][c]
                
                
        return res
