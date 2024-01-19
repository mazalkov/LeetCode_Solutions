class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        
        ROWS = len(matrix)
        COLS = len(matrix[0])
        MAX = 2 ** 16

        dp = [[MAX] * COLS for _ in range(ROWS)]

        for col in range(COLS):
            dp[0][col] = matrix[0][col]

        for row in range(1, ROWS):
            for col in range(COLS):
                prev_min = dp[row-1][col]

                if col - 1 >= 0:
                    prev_min = min(prev_min, dp[row-1][col-1])

                if col + 1 < ROWS:
                    prev_min = min(prev_min, dp[row-1][col+1])

                dp[row][col] = prev_min + matrix[row][col]


        return min(dp[ROWS-1])
