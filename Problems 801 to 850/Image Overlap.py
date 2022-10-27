# https://leetcode.com/problems/image-overlap

# Runtime: 323 ms, faster than 97.66% of Python3 online submissions for Image Overlap.
# Excellent runtime, considerably better than brute force as only existing values are checked.

# Memory Usage: 14 MB, less than 88.30% of Python3 online submissions for Image Overlap.
# Excellent memory usage, the count list of lists isn't too large comparable to other solutions.


class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        # thanks to: https://wentao-shao.gitbook.io/leetcode/matrix/835.image-overlap

        N = len(img1)
        
        count = [[0 for _ in range((2*N)+1)] for _ in range((2*N)+1)]
        
        for i in range(N):
            for j in range(N):
                if img1[i][j]:
                    for x in range(N):
                        for y in range(N):
                            if img2[x][y]:
                                count[i-x+N][j-y+N] += 1
                                

        return max(item for sublist in count for item in sublist)   
