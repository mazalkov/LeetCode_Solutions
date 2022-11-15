# https://leetcode.com/problems/count-complete-tree-nodes

# Runtime: 86 ms, faster than 91.72% of Python3 online submissions for Count Complete Tree Nodes.
# Excellent runtime, doing tbe left/right completeness check should save time on the average case.

# Memory Usage: 21.3 MB, less than 86.80% of Python3 online submissions for Count Complete Tree Nodes.
# Excellent memory usage, garbage collector should handle anything unused, nothing is unnecessary. 


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
# thanks to: https://www.geeksforgeeks.org/count-number-of-nodes-in-a-complete-binary-tree/
    def countNodes(self, root: Optional[TreeNode]) -> int:
        
        def left_h(node):
            h = 0
            while node:
                h += 1
                node = node.left
                
            return h
    
    
        def right_h(node):
            h = 0
            while node:
                h += 1
                node = node.right
                
            return h
        
        
        def total(root):
            if not root:
                return 0
            
            l_h = left_h(root)
            r_h = right_h(root)
            
            
            if l_h == r_h:
                return (1 << l_h) - 1
            
            
            return 1 + total(root.left) + total(root.right)
        
        return total(root)
