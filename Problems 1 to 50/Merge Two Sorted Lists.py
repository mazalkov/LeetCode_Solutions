# https://leetcode.com/problems/merge-two-sorted-lists

# Runtime: 44 ms, faster than 70.31% of Python3 online submissions for Merge Two Sorted Lists.
# Decent runtime, not very proficient at traversing lists at time of writing, but speed is acceptable.

# Memory Usage: 13.8 MB, less than 89.81% of Python3 online submissions for Merge Two Sorted Lists.
# Great memory usage, only defining variables necessary for traversing the list, nothing else is needed.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # thanks to NeetCode for this solution: https://youtu.be/XIdigk956u0
        dummy = ListNode()
        tail = dummy
        
        while list1 and list2:
            
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
                
            else:
                tail.next = list2
                list2 = list2.next
                
            tail = tail.next
            
        
        if list1:
            tail.next = list1
        
        if list2:
            tail.next = list2
            
            
        return dummy.next
