"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        
        if not root:
            return
        
        level = [root]
        
        while level:
            
            for i in range(1, len(level)):
                level[i-1].next = level[i]
            level[-1].next = None
            
            level = [(node.left, node.right) for node in level]
            level = [node for nodepair in level for node in nodepair if node]
            
        return root
        