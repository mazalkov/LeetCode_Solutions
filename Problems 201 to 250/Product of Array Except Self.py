class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        LENGTH = len(nums)
        res = [1]*LENGTH

        left_product = 1
        for i in range(LENGTH):
            res[i] = left_product
            left_product *= nums[i]

        right_product = 1
        for i in range(LENGTH-1, -1, -1):
            res[i] *= right_product
            right_product *= nums[i]

        return res
