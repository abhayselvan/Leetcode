# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        
        if not root:
            return 0
        
        return self._maxDepth(root, 1)
    
    def _maxDepth(self, node, depth):
        
        if not node.left and not node.right:
            return depth
        
        if node.left and node.right:
            return max(self._maxDepth(node.left, depth+1), self._maxDepth(node.right, depth+1))
        
        if node.left:
            return self._maxDepth(node.left, depth+1)
            
        if node.right:
            return self._maxDepth(node.right, depth+1)
            