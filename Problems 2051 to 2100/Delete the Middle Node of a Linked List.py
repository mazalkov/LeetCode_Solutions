# https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list

# Runtime: 1727 ms, faster than 98.85% of Python3 online submissions for Delete the Middle Node of a Linked List.
# Excellent runtime, was worried that the two checks for count would be slow, but rest of algorithm seems decent.

# Memory Usage: 60.6 MB, less than 79.89% of Python3 online submissions for Delete the Middle Node of a Linked List.
# Good memory usage, storing a temporary variable allows us to find the linked list length, counter and mid also needed.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # thanks to: https://www.alphacodingskills.com/python/ds/python-count-nodes-in-the-linked-list.php
        # also used my previous solution to https://leetcode.com/problems/delete-node-in-a-linked-list/
        
        temp = head
        count = 0
        
        while temp != None:
            count += 1
            temp = temp.next
        temp = head
        
        if count == 1:
            return None
        
        if count < 3:
            temp.next = None
            return head
            
        mid = count // 2
        
        for _ in range(mid):
            temp = temp.next
            
        temp.val = temp.next.val
        temp.next = temp.next.next
        
        
        return head
