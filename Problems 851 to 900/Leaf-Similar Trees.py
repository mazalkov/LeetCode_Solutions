# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        def dfs(node, seq):
            if not node:
                return

            if not node.left and not node.right:
                seq.append(node.val)
                return

            dfs(node.left, seq)
            dfs(node.right, seq)


        leaves_1, leaves_2 = [], []
        dfs(root1, leaves_1)
        dfs(root2, leaves_2)

        return leaves_1 == leaves_2
