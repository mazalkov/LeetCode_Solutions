# https://leetcode.com/problems/intersection-of-two-linked-lists

# Runtime: 160 ms, faster than 93.54% of Python3 online submissions for Intersection of Two Linked Lists.
# Excellent runtime, this algorithm seems very efficient and a suitable alternative to using Floyd's algorithm.

# Memory Usage: 29.5 MB, less than 93.75% of Python3 online submissions for Intersection of Two Linked Lists.
# Excellent memory usage, only having to store pointers to the original heads to use in case of returning.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # thanks to: https://youtu.be/D0X0BONOQhI
        
        l1, l2 = headA, headB
        
        # while no intersection:
        while l1 != l2:
          
            # advance l1 if possible, otherwise
            # point to head of linked list B
            l1 = l1.next if l1 else headB
            
            # advance l2 if possible, otherwise
            # point to head of linked list A
            l2 = l2.next if l2 else headA
            
            
        # these will eventually "meet" at the intersection point,
        # or if no such point exists, will meet at 'null' to return
        return l1
