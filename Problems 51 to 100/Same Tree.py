# https://leetcode.com/problems/same-tree

# Runtime: 46 ms, faster than 40.98% of Python3 online submissions for Same Tree.
# Below average runtime, the structure of the checks as well as recursion may be causing this.

# Memory Usage: 13.8 MB, less than 98.63% of Python3 online submissions for Same Tree.
# Excellent memory usage, no need to store extra variables, only a stack of function calls.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # thanks to: https://www.programcreek.com/2012/12/check-if-two-trees-are-same-or-not/
        
        if not p and not q:
            return True
        
        elif not p or not q:
            return False
        
        elif p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
        else:
            return False
