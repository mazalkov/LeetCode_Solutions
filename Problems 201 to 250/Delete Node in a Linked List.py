# https://leetcode.com/problems/delete-node-in-a-linked-list

# Runtime: 44 ms, faster than 89.11% of Python3 online submissions for Delete Node in a Linked List.
# Excellent runtime, only need to do two operations on one node, thanks to video for clever method

# Memory Usage: 14.2 MB, less than 91.10% of Python3 online submissions for Delete Node in a Linked List.
# Excellent memory usage, no need to store anything, just modify the node values in-place


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # thanks to: https://youtu.be/bJPmNKMtjdk
        
        node.val = node.next.val
        node.next = node.next.next
