# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        
        MAX = 2 ** 64
        res = 0

        def traverse(node, high, low):
            if node is None:
                return

            nonlocal res
            res = max(res, high - node.val)
            res = max(res, node.val - low)

            high = max(high, node.val)
            low = min(low, node.val)

            traverse(node.left, high, low)
            traverse(node.right, high, low)

        traverse(root, -MAX, MAX)
        return res
