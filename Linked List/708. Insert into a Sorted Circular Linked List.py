"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        
        new_node = Node(insertVal)
        
        if not head:
            new_node.next = new_node
            return new_node
        
        prev, curr = head, head.next
        
        insert = False
        
        while True:
            
            if prev.val <= insertVal <= curr.val:
                insert = True
                
            elif prev.val > curr.val:
                if insertVal >= prev.val or insertVal <= curr.val:
                    insert = True
                    
            if insert:
                prev.next = new_node
                new_node.next = curr
                return head
            
            prev, curr = curr, curr.next
            
            if prev == head:
                break
                
        prev.next = new_node
        new_node.next = curr
        
        return head
                
            