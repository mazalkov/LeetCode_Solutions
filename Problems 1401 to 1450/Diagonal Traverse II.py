class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        
        ROWS = len(nums)
        res = []

        for x in range(ROWS):
            for y in range(len(nums[x])):
                res.append((x+y, y, nums[x][y]))

        res = list(item[2] for item in sorted(res))
        return res
