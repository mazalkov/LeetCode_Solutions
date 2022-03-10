# https://leetcode.com/problems/reshape-the-matrix

# Runtime: 156 ms, faster than 26.08% of Python3 online submissions for Reshape the Matrix.
# Poor runtime, using Numpy functions is likely the cause, but this is arguably more readable.

# Memory Usage: 32.6 MB, less than 5.11% of Python3 online submissions for Reshape the Matrix.
# Very poor memory usage, once again this is probably attributed to the use of Numpy functions.


import numpy as np


class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        
        n, m = len(mat[0]), len(mat)
        
        if n*m != r*c:
            return mat
        else:
            return np.reshape(mat, [r, c])
