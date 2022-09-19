# https://leetcode.com/problems/symmetric-tree

# Runtime: 62 ms, faster than 36.33% of Python3 online submissions for Symmetric Tree.
# Poor runtime, tried to make a slight optimisation to the conditional check, slow overall.

# Memory Usage: 13.9 MB, less than 93.86% of Python3 online submissions for Symmetric Tree.
# Excellent memory usage, no need to store or pass variables unnecessarily beyond the two nodes.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
# thanks to: https://youtu.be/-5E5Jt_HKLc
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def isMirror(t1, t2):
            if t1 == None and t2 == None: return True
            elif t1 == None or t2 == None: return False

            else:
                return (t1.val == t2.val) and isMirror(t1.left, t2.right) and isMirror(t1.right, t2.left)
        
        return isMirror(root, root)
