# https://leetcode.com/problems/binary-search-tree-iterator

# Runtime: 74 ms, faster than 87.94% of Python3 online submissions for Binary Search Tree Iterator.
# Excellent runtime, this should be one of the fastest implementations using the OOP principles outlined.

# Memory Usage: 20.3 MB, less than 63.85% of Python3 online submissions for Binary Search Tree Iterator.
# Decent memory usage, using a cursor may be unnecessary, along with the approach itself being inefficient on average.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    # thanks to: https://youtu.be/RXy5RzGF5wo

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        
        while root:
            self.stack.append(root)
            root = root.left
            

    def next(self) -> int:
        res = self.stack.pop()
        
        cur = res.right
        while cur:
            self.stack.append(cur)
            cur = cur.left
        return res.val
        

    def hasNext(self) -> bool:
        return self.stack 


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
