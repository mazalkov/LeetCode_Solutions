# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        res = 0
        max_depth = -1

        def search(node, depth):
            if node is None:
                return 

            search(node.left, depth+1)
            search(node.right, depth+1)

            nonlocal max_depth
            if depth > max_depth:
                max_depth = depth
                
                nonlocal res
                res = node.val

        search(root, 0)
        return res
