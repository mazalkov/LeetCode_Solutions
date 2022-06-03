# https://leetcode.com/problems/range-sum-query-2d-immutable

# Runtime: 2213 ms, faster than 45.63% of Python3 online submissions for Range Sum Query 2D - Immutable.
# Average runtime, while this is likely faster than manually looping over that area, the setup is very long.

# Memory Usage: 24.9 MB, less than 69.33% of Python3 online submissions for Range Sum Query 2D - Immutable.
# Decent memory usage, creating an extra dp array to store running sums is not efficient but still good for setup.


class NumMatrix:
    # thanks to: https://youtu.be/KE8MQuwE2yA

    def __init__(self, matrix: List[List[int]]):
        ROWS, COLS = len(matrix), len(matrix[0])
        # initialise a dp array with padded zeros at top and left
        self.dp = [[0]*(COLS+1) for row in range(ROWS+1)]
        
        for row in range(ROWS):
            running_sum = 0
            
            for col in range(COLS):
                running_sum += matrix[row][col]
                above_sum = self.dp[row][col+1]
                self.dp[row+1][col+1] = running_sum + above_sum
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:

        # dp array has been top and left padded:
        total_sum = self.dp[row2+1][col2+1]
        above_portion = self.dp[row1][col2+1]
        left_portion = self.dp[row2+1][col1]
        extra_portion = self.dp[row1][col1]
        
        
        return total_sum - (above_portion + left_portion - extra_portion)


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
