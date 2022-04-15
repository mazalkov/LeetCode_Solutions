# https://leetcode.com/problems/trim-a-binary-search-tree

# Runtime: 53 ms, faster than 82.07% of Python3 online submissions for Trim a Binary Search Tree.
# Good runtime, recursively trimming each side until only the final subtree remains seems fast.

# Memory Usage: 18 MB, less than 83.03% of Python3 online submissions for Trim a Binary Search Tree.
# Good memory usage, no need to define extra variables, however recursive calls may use a lot of memory.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        # thanks to: https://youtu.be/jwt5mTjEXGc
        
        if not root:
            return None
        
        if root.val > high:
            return self.trimBST(root.left, low, high)
        
        if root.val < low:
            return self.trimBST(root.right, low, high)
        
        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)
        
        return root
