# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:

        res = []
        
        if not root:
            return res

        q = collections.deque([root])

        while q:
            max_seen = -sys.maxsize-1

            for _ in range(len(q)):
                top_level = q.popleft()

                max_seen = max(max_seen, top_level.val)

                if top_level.left:
                    q.append(top_level.left)

                if top_level.right:
                    q.append(top_level.right)

            res.append(max_seen)

        return res       
