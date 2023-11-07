class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:

        res = 0
        # Take ceiling as weapon is used at every minute interval
        minute_reached = [math.ceil(x/y) for x, y in zip(dist, speed)]
        minute_reached.sort()

        # i is used as a proxy for the "timer" in minutes
        for i in range(len(minute_reached)):
            if i >= minute_reached[i]:
                return res
            else:
                res += 1

        return res
