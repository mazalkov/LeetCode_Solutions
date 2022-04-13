# https://leetcode.com/problems/spiral-matrix-ii

# Runtime: 38 ms, faster than 72.82% of Python3 online submissions for Spiral Matrix II.
# Pretty good runtime, list comprehension at the start may save time over dynamic allocation.

# Memory Usage: 14 MB, less than 41.06% of Python3 online submissions for Spiral Matrix II.
# Below average memory usage, a few variables are used for readability despite being unnecessary.


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        res = [[0]*n for i in range(n)]
        
        row_begin = 0
        row_end = n-1
        col_begin = 0
        col_end = n-1
        
        counter = 1
        
        while (row_begin <= row_end) and (col_begin <= col_end):
            
            for i in range(col_begin, col_end+1):
                res[row_begin][i] = counter
                counter += 1
            row_begin += 1
            
            for i in range(row_begin, row_end+1):
                res[i][col_end] = counter 
                counter += 1
            col_end -= 1
            
            if row_begin <= row_end:
                for i in range(col_end, col_begin-1, -1):
                    res[row_end][i] = counter
                    counter += 1
            row_end -= 1
            
            if col_begin <= col_end:
                for i in range(row_end, row_begin-1, -1):
                    res[i][col_begin] = counter
                    counter += 1
            col_begin += 1
            
            
        return res
