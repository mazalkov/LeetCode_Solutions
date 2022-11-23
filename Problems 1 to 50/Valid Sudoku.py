# https://leetcode.com/problems/valid-sudoku

# Runtime: 213 ms, faster than 53.94% of Python3 online submissions for Valid Sudoku.
# Average runtime, this is quite a verbose and brute force method but does the job.

# Memory Usage: 13.8 MB, less than 99.18% of Python3 online submissions for Valid Sudoku.
# Excellent memory usage, using sets and only the board makes this more space efficient.


class Solution:
# thanks to NeetCode
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set)
        
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                    
                if board[r][c] in rows[r] or \
                board[r][c] in cols[c] or \
                board[r][c] in squares[(r // 3, c // 3)]:
                    return False
                
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])
                
                
        return True
