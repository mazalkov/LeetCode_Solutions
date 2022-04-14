# https://leetcode.com/problems/search-in-a-binary-search-tree

# Runtime: 69 ms, faster than 97.31% of Python3 online submissions for Search in a Binary Search Tree.
# Excellent runtime, although a recursive solution it is likely quick due to the tree being sorted.

# Memory Usage: 16.4 MB, less than 74.05% of Python3 online submissions for Search in a Binary Search Tree.
# Good memory usage, recursive solutions may create a lot of function calls to the stack, still good overall.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # thanks to: https://ibrahimhasnat.com/700-search-in-a-binary-search-tree-leetcode-python-solution/
        
        if not root: return None
        if root.val == val: return root
        
        if val < root.val:
            return self.searchBST(root.left, val)
        
        else:
            return self.searchBST(root.right, val)
