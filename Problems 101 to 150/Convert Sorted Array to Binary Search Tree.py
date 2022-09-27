# https://www.geeksforgeeks.org/sorted-array-to-balanced-bst

# Runtime: 159 ms, faster than 15.52% of Python3 online submissions for Convert Sorted Array to Binary Search Tree.
# Very poor runtime, this recursive approach is likely the reason why, need to investigate binary search trees further.

# Memory Usage: 15.5 MB, less than 82.50% of Python3 online submissions for Convert Sorted Array to Binary Search Tree.
# Good memory usage, need to go over use of self object within classes again, is this memory required to be sent across.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
    # thanks to: https://www.geeksforgeeks.org/sorted-array-to-balanced-bst/    
  
        if not nums:
            return None
        
        mid = len(nums) // 2
        
        root = TreeNode(nums[mid])
        
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        
        
        return root
