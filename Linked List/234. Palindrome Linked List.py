# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        
        slow = fast = head
        
        while fast and fast.next:
            
            slow = slow.next
            fast = fast.next.next
            
        rev = None
        curr = head
        
        while curr != slow:
            nxt = curr.next
            curr.next = rev
            rev = curr
            curr = nxt
            
        if fast:
            slow = slow.next
            
        while rev and slow:
            
            print(slow.val, rev.val)
            if rev.val != slow.val:
                return False
            
            rev = rev.next
            slow = slow.next
            
        return not rev and not slow
            
            
            
            
        
            