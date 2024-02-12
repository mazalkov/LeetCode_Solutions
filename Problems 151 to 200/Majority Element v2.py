class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        res, offset = 0, 0

        for n in nums:
            if offset == 0:
                res = n

            if res == n:
                offset += 1

            else:
                offset -= 1

        return res
