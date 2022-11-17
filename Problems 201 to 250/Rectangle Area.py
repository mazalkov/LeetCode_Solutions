# https://leetcode.com/problems/rectangle-area

# Runtime: 58 ms, faster than 89.86% of Python3 online submissions for Rectangle Area.
# Excellent runtime, seems like a fast algorithm, the min max comparisons could be neater.

# Memory Usage: 13.9 MB, less than 98.16% of Python3 online submissions for Rectangle Area.
# Near perfect memory usage, minimum variables used and garbage collector can take care of them.


class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        
        area_a = (ax2 - ax1) * (ay2 - ay1)
        area_b = (bx2 - bx1) * (by2 - by1) 
        
        overlap_x = min(ax2,bx2) - max(ax1,bx1)
        overlap_y = min(ay2, by2) - max(ay1,by1)
        
        overlap_x, overlap_y = max(overlap_x, 0), max(overlap_y, 0)

        
        return (area_a + area_b) - (overlap_x * overlap_y)
