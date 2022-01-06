# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        num1, num2 = 0, 0
        places1, places2 = 0, 0
        
        while l1 is not None:
            num1 += l1.val * 10**places1
            l1 = l1.next
            places1 += 1
            
        while l2 is not None:
            num2 += l2.val * 10**places2
            l2 = l2.next
            places2 += 1

        result = num1 + num2
        l = [int(digit) for digit in str(result)]
        
        cur = dummy_node = ListNode(0)
        for elem in l[::-1]:
            cur.next = ListNode(elem)
            cur = cur.next
            
            
        return dummy_node.next
