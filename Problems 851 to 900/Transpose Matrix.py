# https://leetcode.com/problems/transpose-matrix

# Runtime: 98 ms, faster than 51.20% of Python3 online submissions for Transpose Matrix.
# Average runtime, this method creates an empty matrix and manually fills one by one after.

# Memory Usage: 14.7 MB, less than 55.25% of Python3 online submissions for Transpose Matrix.
# Average memory usage, could be a way to modify in-place but could be at cost of speed.


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        
        M, N = len(matrix), len(matrix[0])
        res = [([None]*M) for _ in range(N)]
        
        for i in range(M):
            for j in range(N):
                res[j][i] = matrix[i][j]
                
                
        return res
