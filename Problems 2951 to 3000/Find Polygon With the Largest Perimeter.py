class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        
        LENGTH = len(nums)
        nums.sort()
        res = -1
        cur = nums[0] + nums[1]
      
        for i in range(2, LENGTH):
            if cur > nums[i]:
                res = max(res, cur + nums[i])
            cur += nums[i]

        return res
