# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        
        prev = ListNode()
        prev.next = head
        
        first = second = prev
        
        for i in range(n+1):
            first = first.next
            
        while first:
            first = first.next
            second = second.next
            
        second.next = second.next.next
        
        return prev.next
            
            