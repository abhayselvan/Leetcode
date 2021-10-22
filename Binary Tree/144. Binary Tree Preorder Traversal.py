# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        
        ans = []
        self.__traverse(root, ans)
        return ans
        
    def __traverse(self, root, ans):
        
        if not root:
            return
        
        ans.append(root.val)
        self.__traverse(root.left, ans)
        self.__traverse(root.right, ans)