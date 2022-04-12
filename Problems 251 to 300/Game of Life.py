# https://leetcode.com/problems/game-of-life

# Runtime: 40 ms, faster than 71.83% of Python3 online submissions for Game of Life.
# Above average runtime, the implementation of the helper function could be optimised.

# Memory Usage: 13.9 MB, less than 93.38% of Python3 online submissions for Game of Life.
# Excelent memory usage, was expecting worse performance even for O(1) but this is acceptable.


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead. (Massive help from: https://youtu.be/fei4bJQdBUQ)
        """
        rows, cols = len(board), len(board[0])
        
        def neighborHelper(r, c):
            neighbors = 0
            
            for i in range(r-1, r+2):
                for j in range(c-1, c+2):
                    
                    if ((i == r and j==c) or i<0 or j<0 or i==rows or j==cols):
                        continue
                        
                    if board[i][j] in [1,3]:
                        neighbors += 1
                        
            return neighbors
        
        
        for r in range(rows):
            for c in range(cols):
                n = neighborHelper(r, c)
                
                if board[r][c]:
                    if n in [2,3]:
                        board[r][c] = 3
                
                # else if a zero has 3 neighbors
                elif n == 3:
                    board[r][c] = 2
                    
                    
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 1:
                    board[r][c] = 0
                    
                elif board[r][c] in [2,3]:
                    board[r][c] = 1
