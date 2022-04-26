# https://leetcode.com/problems/flipping-an-image

# Runtime: 54 ms, faster than 79.92% of Python3 online submissions for Flipping an Image.
# Good runtime, list comprehension with bitwise XOR seems to be a fast way of flipping.

# Memory Usage: 13.9 MB, less than 67.35% of Python3 online submissions for Flipping an Image.
# Okay memory usadge, doing enumerate may be taking up a lot of memory for indices and items.


class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        
        for i, l in enumerate(image):
            image[i] = [bit^1 for bit in l[::-1]]
            
            
        return image
