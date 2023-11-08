class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        
        dx = abs(sx - fx)
        dy = abs(sy - fy)

        # edge case
        if (dx == 0) and (dy == 0) and (t == 1):
            return False

        # general case as we can move diagonally
        if (t < dx) or (t < dy):
            return False

        return True
