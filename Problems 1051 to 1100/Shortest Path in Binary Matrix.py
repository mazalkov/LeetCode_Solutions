# https://leetcode.com/problems/shortest-path-in-binary-matrix

# Runtime: 603 ms, faster than 90.36% of Python3 online submissions for Shortest Path in Binary Matrix.
# Excellent runtime, this BFS algorithm seems to handle the matrix quickly, especially by changing in-place.

# Memory Usage: 14.3 MB, less than 79.31% of Python3 online submissions for Shortest Path in Binary Matrix.
# Good memory usage, modifying in-place may not be allowed but saves from having to have a visited set.


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # thanks to: https://youtu.be/vn-Jol8SNsM
        
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        
        dirs = [(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1)]
        
        if grid[0][0] == 0:
            q.append((1, (0, 0)))
            grid[0][0] = 1
            
        while q:
            steps, temp_pos = q.popleft()
            r, c = temp_pos[0], temp_pos[1]
            
            if (r, c) == (ROWS-1, COLS-1):
                return steps
            
            for i, j in dirs:
                new_r, new_c = r+i, c+j
                
                if (0<= new_r < ROWS) and (0<= new_c < COLS) and (grid[new_r][new_c] == 0):
                    q.append((steps+1, (new_r, new_c)))
                    grid[new_r][new_c] = 1
                    
        return -1
