# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons

# Runtime: 2628ms, Beats: 45.84% 
# Average runtime, this appears to be a slow algorithm, could use range intersection

# Memory: 59.9.MB, Beats: 69.76% 
# Good memory usage, only sorting the list in-place and using some temp variables.


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:

        length = len(points)
        if length == 1:
            return 1

        res = 1
        points.sort()
    
        prev = points[0][1]

        for i in range(length):
            if prev < points[i][0]:
                res += 1
                prev = points[i][1]

            prev = min(prev, points[i][1])

            
        return res
