# https://leetcode.com/problems/linked-list-cycle

# Runtime: 78 ms, faster than 52.02% of Python3 online submissions for Linked List Cycle.
# Not great, average runtime likely owing to the algorithm complexity used, need to learn more.

# Memory Usage: 17.6 MB, less than 42.75% of Python3 online submissions for Linked List Cycle.
# Below average memory usage, the fast pointer is likely bloating the memory and could use rework.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# with a lot of help from: https://youtu.be/gBTe7lFR3vc
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        slow, fast = head, head
        
        while fast and fast.next:
            
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                return True
            
            
        return False
