class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        pos_idx, neg_idx = 0, 1
        for n in nums:
            if n > 0:
                res[pos_idx] = n
                pos_idx += 2
            else:
                res[neg_idx] = n
                neg_idx += 2

        return res
