# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def __init__(self):
        self.memo = {0:[], 1:[TreeNode()]}
        
    def allPossibleFBT(self, n: int) -> List[TreeNode]:
        
        if n % 2 == 0:
            return []
        
        if n not in self.memo:
            res = []
            for i in range(1,n,2):
                for left in self.allPossibleFBT(i):
                    for right in self.allPossibleFBT(n-i-1):
                        node = TreeNode()
                        node.left = left
                        node.right = right
                        res.append(node)
            self.memo[n] = res
            
        return self.memo[n]
            
        
        
        
        
        