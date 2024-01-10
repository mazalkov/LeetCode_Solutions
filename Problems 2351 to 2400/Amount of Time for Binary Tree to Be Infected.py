# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        
        def connect_parent(node, parent):
            if node is None:
                return

            node.parent = parent

            connect_parent(node.left, node)
            connect_parent(node.right, node)

        connect_parent(root, None)

        found = None
        def find_node(node):
            if node is None:
                return

            if node.val == start:
                nonlocal found
                found = node

            find_node(node.left)
            find_node(node.right)

        find_node(root)
        assert(found is not None)

        farthest = 0

        def find_farthest(node, prev, h):
            farthest = 0
            for next_node in [node.left, node.right, node.parent]:
                if next_node != prev and next_node is not None:
                    farthest = max(farthest, find_farthest(next_node, node, h+1)+1)
            return farthest


        return find_farthest(found, None, 0)
