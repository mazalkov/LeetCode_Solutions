class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        count = 0
        
        for i, elem in enumerate(nums):
            if elem != val:
                nums[count] = nums[i]
                count += 1
                
                
        return count
