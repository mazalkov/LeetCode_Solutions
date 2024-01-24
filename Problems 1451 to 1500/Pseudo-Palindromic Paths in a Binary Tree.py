# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        
        def traverse(node, counter):
            if node is None:
                return 0

            counter[node.val] += 1

            res = 0
            if node.left is None and node.right is None:
                valid = sum(v % 2 for v in counter.values()) <= 1
                res += int(valid)
            else:
                res += traverse(node.left, counter)
                res += traverse(node.right, counter)

            counter[node.val] -= 1
            if counter[node.val] == 0:
                del counter[node.val]

            return res

        return traverse(root, Counter())
