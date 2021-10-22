# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        
        if not root: return []
        
        level = [root]
        ans = []
        
        while level:
            
            ans.append([node.val for node in level])
            level = [(node.left, node.right) for node in level]
            level = [node for nodepair in level for node in nodepair if node]
            
        return ans
            