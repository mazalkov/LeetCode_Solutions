# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.res = []
        self.previous = None
        self.count, self.max_count = 0, 0

        def update_count(root):
            if self.previous and self.previous.val == root.val:
                self.count += 1
            else:
                self.count = 1

            if self.count > self.max_count:
                self.max_count = self.count
                self.res = [root.val]
            elif self.count == self.max_count:
                self.res.append(root.val)

            self.previous = root

        
        def traverse_inorder(root):
            if not root:
                return

            traverse_inorder(root.left)
            update_count(root)
            traverse_inorder(root.right)

        traverse_inorder(root)
        return self.res
