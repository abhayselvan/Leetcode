# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        
        inorder_list = []
        self._inorderTraversal(root, inorder_list)
        return inorder_list
    
    def _inorderTraversal(self, node, inorder_list):
    
        if not node:
            return
        
        self._inorderTraversal(node.left, inorder_list)
        inorder_list.append(node.val)
        self._inorderTraversal(node.right, inorder_list)
        