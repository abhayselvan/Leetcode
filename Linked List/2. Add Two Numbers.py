# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
       
        head = curr = prev = ListNode()
        carry = 0
        
        
        while l1 or l2 or carry:
            
            if l1:
                curr.val += l1.val
                l1 = l1.next
                
            if l2:
                curr.val += l2.val
                l2 = l2.next
                
            if carry:
                curr.val += carry
                carry = 0
                
            if curr.val > 9:
                carry = 1
                curr.val %= 10
                
            prev = curr
            curr.next = ListNode()
            curr = curr.next
            
        if curr.val == 0:
            prev.next = None
            
        return head