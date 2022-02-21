# https://leetcode.com/problems/construct-the-rectangle

# Runtime: 36 ms, faster than 79.35% of Python3 online submissions for Construct the Rectangle.
# Pretty good runtime, having the while loop may not be as efficient as a Diophantine solution.

# Memory Usage: 13.8 MB, less than 98.76% of Python3 online submissions for Construct the Rectangle.
# Excellent memory usage, only defining width and decrementing in a while loop. May be quicker with a formula.


class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        
        # adapted from https://dilyar85.gitbooks.io/leetcode-solutions-with-analysis/content/Problems/492_construct_the_rectangle_java.html
        
        width = int(area**0.5)
        
        while area % width:
            width -= 1
            
            
        return [area // width, width]
