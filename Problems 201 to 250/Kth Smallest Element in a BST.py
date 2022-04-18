# https://leetcode.com/problems/kth-smallest-element-in-a-bst

# Runtime: 45 ms, faster than 96.55% of Python3 online submissions for Kth Smallest Element in a BST.
# Excellent runtime, iterative solution over recursive, so there may be speed advantages for Leetcode.

# Memory Usage: 17.9 MB, less than 99.08% of Python3 online submissions for Kth Smallest Element in a BST.
# Excellent memory usage, only storing a counter, cursor/pointer and a stack of traversed tree nodes.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # thanks to: https://youtu.be/5LUXSvjmGCw
        
        visited = 0
        stack = []
        cur = root
        
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
                
            cur = stack.pop()
            visited += 1
            
            if visited == k:
                return cur.val
            else:
                cur = cur.right
