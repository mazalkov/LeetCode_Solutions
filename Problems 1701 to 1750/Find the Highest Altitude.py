class Solution:
    def largestAltitude(self, gain: List[int]) -> int:

        current_alt = 0
        res = 0

        for num in gain:
            current_alt += num
            res = max(res, current_alt)


        return res
