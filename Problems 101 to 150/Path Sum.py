# https://leetcode.com/problems/path-sum

# Runtime: 48 ms, faster than 76.39% of Python3 online submissions for Path Sum.
# Good runtime, depth-first search with sum checks seems to be an adequate algorithm.

# Memory Usage: 14.9 MB, less than 99.67% of Python3 online submissions for Path Sum.
# Near perfect memory usage, only having to store and pass through the current sum.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        # thanks to: https://youtu.be/LSKQyOz_P8I
        
        def dfs(node, cur_sum):
            if not node:
                return False
            
            cur_sum += node.val
            
            if not node.left and not node.right:
                return cur_sum == targetSum
            
            return dfs(node.left, cur_sum) or dfs(node.right, cur_sum)
        
        
        return dfs(root, 0)
