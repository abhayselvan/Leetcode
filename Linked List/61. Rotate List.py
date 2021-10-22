# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        
        if not head:
            return
        
        size = 1
        curr = head
        
        while curr and curr.next:
            size += 1
            curr = curr.next
            
        last = curr
        
        curr = head
        for i in range(size - (k % size) - 1):
            
            curr = curr.next
        
        if curr and curr.next:
            new_head = curr.next
            curr.next = None
            last.next = head

            return new_head
        
        return head