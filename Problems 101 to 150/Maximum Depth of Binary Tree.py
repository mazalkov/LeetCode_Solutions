# https://leetcode.com/problems/maximum-depth-of-binary-tree

# Runtime: 74 ms, faster than 44.18% of Python3 online submissions for Maximum Depth of Binary Tree.
# Not great runtime, perhaps using the function through the class and passing self is slowing down.

# Memory Usage: 16.1 MB, less than 74.53% of Python3 online submissions for Maximum Depth of Binary Tree.
# Good memory usage, no need to define or store any extra unnecessary variables, only storing depths.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # thanks to: https://www.educative.io/answers/finding-the-maximum-depth-of-a-binary-tree
                
        if not root:
            return 0
        
        left_depth = Solution.maxDepth(self, root.left)
        right_depth = Solution.maxDepth(self, root.right)
        
        if left_depth > right_depth:
            return left_depth + 1
        
        else:
            return right_depth + 1
