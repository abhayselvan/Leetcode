"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        
        nodes = {}
        curr = head
        
        new_node = None
        new_curr = new_head = Node(0)
        
        
        while curr:
            
            new_node = Node(curr.val)
            new_curr.next = new_node
            
            nodes[curr] = new_node
            
            if curr.next:
                nxt = Node(curr.next.val)
                new_node.next = nxt
                
            curr = curr.next
            new_curr = new_curr.next
            
        curr = head
        new_curr = new_head.next
        
        while curr:
            
            random = nodes.get(curr.random)
            new_curr.random = random
            
            curr = curr.next
            new_curr = new_curr.next
            
        return new_head.next