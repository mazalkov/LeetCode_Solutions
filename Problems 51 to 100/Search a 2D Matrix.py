# https://leetcode.com/problems/search-a-2d-matrix

# Runtime: 48 ms, faster than 84.58% of Python3 online submissions for Search a 2D Matrix.
# Good runtime, performing a binary search both times should be the most optimal solution.

# Memory Usage: 14.3 MB, less than 90.46% of Python3 online submissions for Search a 2D Matrix.
# Excellent memory usage, only tracking lengths and binary search pointers, nothing else needed.


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # greatly helped by: https://youtu.be/Ber2pi2C0j0    
          
        ROWS, COLS = len(matrix), len(matrix[0])
        
        top, bottom = 0, ROWS-1
        
        while top <= bottom:
            row = (top + bottom) // 2
            
            if target > matrix[row][-1]:
                top = row + 1
                
            elif target < matrix[row][0]:
                bottom = row - 1
                
            else:
                break
                
        if not (top <= bottom):
            return False
        
        row = (top + bottom) // 2
        left, right = 0, COLS-1
        
        while left <= right:
            mid = (left + right) // 2
            
            if target > matrix[row][mid]:
                left = mid + 1
                
            elif target < matrix[row][mid]:
                right = mid - 1
                
            else:
                return True
            
        return False
