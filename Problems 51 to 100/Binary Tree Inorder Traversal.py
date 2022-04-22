# https://leetcode.com/problems/binary-tree-inorder-traversal

# Runtime: 37 ms, faster than 65.30% of Python3 online submissions for Binary Tree Inorder Traversal.
# Decent runtime, a recurisve solution was chosen for the traversal, although iterative may be faster.

# Memory Usage: 13.7 MB, less than 97.22% of Python3 online submissions for Binary Tree Inorder Traversal.
# Excellent memory usage, only defining one list, then appending based on results of traversal.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        res = []
        
        if root:
            res = self.inorderTraversal(root.left)
            res.append(root.val)
            res += self.inorderTraversal(root.right)
            
            
        return res
