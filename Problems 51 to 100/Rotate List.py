# https://leetcode.com/problems/rotate-list

# Runtime: 55 ms, faster than 49.11% of Python3 online submissions for Rotate List.
# Average runtime, need to read up more on linked lists to know how to improve this.

# Memory Usage: 14 MB, less than 54.84% of Python3 online submissions for Rotate List.
# Average memory usage, defining so many variables is likely a cause of the lower result.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
      
        # with thanks to: https://youtu.be/UcGtPs2LE_c
        
        if not head:
            return head
        
        length, tail = 1, head
        
        while tail.next:
            tail = tail.next
            length += 1
            
        k %= length
        
        if k == 0:
            return head
        
        current = head
        
        for i in range(length-k-1):
            current = current.next
        new_head = current.next
        
        current.next = None
        tail.next = head
        
        
        return new_head
