# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        
        return self.__dfs(root, float('inf'), float('-inf'))
        
    def __dfs(self, root, max_value, min_value):
        
        if not root:
            return True
        
        if root.val >= max_value or root.val <= min_value:
            return False
        
        left = self.__dfs(root.left, root.val, min_value)
        right = self.__dfs(root.right, max_value, root.val)
        
        return left and right