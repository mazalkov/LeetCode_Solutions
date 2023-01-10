# https://leetcode.com/problems/same-tree

# Runtime: 26ms, Beats: 97.28%
# Much better runtime, this is likely achieved by removing a check from the first version.

# Memory: 13.8MB, Beats: 72.95%
# Good memory usage, probably some internal stack creation but nothing explicit.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if not p and not q:
            return True

        if p and q and (p.val == q.val):
            return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)

        else:
            return False
