class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        left = self.binary_search(nums, target, True)
        right = self.binary_search(nums, target, False)
        return [left, right]

    def binary_search(self, nums, target, leftBias):
        left, right = 0, len(nums)-1
        i = -1

        while left <= right:
            mid = (left + right) // 2

            if target > nums[mid]:
                left = mid + 1

            elif target < nums[mid]:
                right = mid - 1

            else:
                i = mid

                if leftBias:
                    right = mid-1

                else:
                    left = mid+1

        return i
