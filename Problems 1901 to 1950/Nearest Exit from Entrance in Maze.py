# https://leetcode.com/problems/nearest-exit-from-entrance-in-maze

# Runtime: 1642 ms, faster than 66.94% of Python3 online submissions for Nearest Exit from Entrance in Maze.
# Average runtime, this algorithm and/or its implementation could be more efficient, need to study maze solving.

# Memory Usage: 15.6 MB, less than 26.78% of Python3 online submissions for Nearest Exit from Entrance in Maze.
# Poor memory usage, too many 'inbetween' variables are used for readability to stop the code becoming messy.


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        
        ROWS = len(maze)
        COLS = len(maze[0])
        
        X, Y = entrance[0], entrance[1]
        
        dirs = [(1,0), (0,1), (-1,0), (0,-1)]
        
        dq = collections.deque()
        dq.append((X, Y))
        
        seen = set()
        
        steps = 0
        
        while dq:
            size = len(dq)
            for _ in range(size):
                i, j = dq.popleft()
                seen.add((i, j))
                
                for di, dj in dirs:
                    i_n = i + di
                    j_n = j + dj
                    
                    if 0 <= i_n < ROWS and \
                    0 <= j_n < COLS and \
                    maze[i_n][j_n] == '.' and \
                    (i_n, j_n) not in seen:
                        
                        if i_n == 0 or \
                        i_n == ROWS-1 or \
                        j_n == 0 or \
                        j_n == COLS-1:
                            
                            return steps+1
                        
                        else:
                            maze[i_n][j_n] = "+"
                            dq.append((i_n, j_n))
                            
            steps += 1
            
        return -1
                    
