class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:

        res = []

        for n in nums:
            res.append(sum([1 for x in nums if x < n]))


        return res
