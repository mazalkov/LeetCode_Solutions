# https://leetcode.com/problems/maximum-ice-cream-bars

# Runtime: 874ms, Beats: 75.92%
# Good runtime, the initial sort may be costly but the for loop is efficient otherwise.

# Memory: 28MB, Beats: 61.26%
# Above average memory usage, only sorting in place and then iterating over a list.


class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:

        res = 0
        costs.sort()

        for c in costs:
            if coins - c >= 0:
                coins -= c
                res += 1
            
            else:
                break


        return res
