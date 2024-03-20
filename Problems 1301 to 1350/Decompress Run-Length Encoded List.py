class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        
        res = []

        for freq, val in list(zip(nums[::2], nums[1::2])):
            res.extend(freq*[val])

        return res
