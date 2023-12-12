class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        a, b = nums[0], nums[1]

        return (a-1) * (b-1)
