# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        res = 0

        def dfs(node):
            if not node:
                return -1

            nonlocal res
            left = dfs(node.left)
            right = dfs(node.right)
            res = max(res, left+right+2)

            return max(left, right) + 1

        dfs(node=root)
        return res
