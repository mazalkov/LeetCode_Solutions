# https://leetcode.com/problems/sort-colors

# Runtime: 40 ms, faster than 72.02% of Python3 online submissions for Sort Colors.
# Good runtime, iterating over the array twice is not optimal but still satisfactory.

# Memory Usage: 13.7 MB, less than 97.45% of Python3 online submissions for Sort Colors.
# Excellent memory usage, only storing occurences for the 3 variables without extras.


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        # thanks to: https://alkeshghorpade.me/post/leetcode-sort-colors
        """
        Do not return anything, modify nums in-place instead.
        """
        red_count, white_count, blue_count = 0, 0, 0
        
        for elem in nums:
            
            if elem == 0:
                red_count +=1
                white_count += 1
                blue_count += 1
            
            elif elem == 1:
                white_count += 1
                blue_count += 1
            
            elif elem == 2:
                blue_count += 1
                
                
        nums[:red_count] = [0] * red_count
        nums[red_count:white_count] = [1] * (white_count-red_count)
        nums[white_count:] = [2] * (len(nums)-white_count)
