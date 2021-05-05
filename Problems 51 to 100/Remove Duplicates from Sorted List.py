# https://leetcode.com/problems/remove-duplicates-from-sorted-list/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        
        # I copied this solution from StackOverflow
        # While I understand the method of how it works
        # I did not write it originally myself
        node = head
        while node:
            lead = node
            while node.next and node.next.val == lead.val:
                node = node.next
            node = lead.next = node.next
        return head
