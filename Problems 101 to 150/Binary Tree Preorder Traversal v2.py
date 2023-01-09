# https://leetcode.com/problems/binary-tree-preorder-traversal

# Runtime: 22ms, Beats: 99.48%
# Near perfect runtime, this implementation seems to integrate well in Python

# Memory: 13.9MB, Beats: 57.18%
# Average memory usage, the stack and root lists are probably not both necessary.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        if root is None:
            return []

        stack = [root]
        res = []
        
        while stack:
            node = stack.pop()
            res.append(node.val)

            if node.right:
                stack.append(node.right)

            if node.left:
                stack.append(node.left)


        return res
