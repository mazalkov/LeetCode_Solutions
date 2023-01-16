# https://leetcode.com/problems/insert-interval

# Runtime: 85ms, Beats: 78.15%
# Excellent runtime, clearly an efficient algorithm, tried my best but had to get help.

# Memory: 17.4MB, Beats 51.90%
# Average memory usage, should be O(n) but could be optimised more for less space.


class Solution:
    # thanks to NeetCode
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        res = []

        for i, interval in enumerate(intervals):
            low, high = newInterval[0], newInterval[1]
            
            if high < interval[0]:
                res.append(newInterval)
                return res + intervals[i:]

            elif low > interval[1]:
                res.append(interval)

            else:
                newInterval = [min(low, interval[0]), max(high, interval[1])]

        res.append(newInterval)
        
        
        return res 
