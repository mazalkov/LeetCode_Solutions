# https://leetcode.com/problems/unique-paths-ii

# Runtime: 42 ms, faster than 90.67% of Python3 online submissions for Unique Paths II.
# Excellent runtime, this implementation of dynamic programming seems to be very efficient.

# Memory Usage: 13.9 MB, less than 74.88% of Python3 online submissions for Unique Paths II.
# Good memory usage, a dynamic array must be stored, but otherwise no unnecessary declarations.


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # thanks to: https://youtu.be/ZqMX18ygGWw
        
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])
        
        dp = [[0 for _ in range(COLS)] for _ in range(ROWS)]
        
        for c in range(COLS):
            if obstacleGrid[0][c]: 
                break
            dp[0][c] = 1
            
        for r in range(ROWS):
            if obstacleGrid[r][0]:
                break
            dp[r][0] = 1
            
        for r in range(1, ROWS):
            for c in range(1, COLS):
                
                if obstacleGrid[r][c]:
                    dp[r][c] = 0
                    
                else:
                    dp[r][c] = dp[r-1][c] + dp[r][c-1]
                    
                    
        return dp[-1][-1]
