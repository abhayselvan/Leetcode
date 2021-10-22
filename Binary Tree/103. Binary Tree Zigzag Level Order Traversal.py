# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        
        if not root:
            return
        
        level = [root]
        ans = []
        count = 0
        
        while level:
            
            if count % 2 == 0:
                ans.append([node.val for node in level])
            else:
                ans.append([node.val for node in level[::-1]])
                
            children = [(node.left, node.right) for node in level]
            level = [node for nodepair in children for node in nodepair if node]
            
            count += 1
            
        return ans