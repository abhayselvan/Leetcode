class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        
        self.memo = {}
        self.matrix = matrix
        
        min_sum = float('inf')
        
        for i in range(len(self.matrix[0])):
            min_sum = min(min_sum, self.minPath(0, i))
            
        return min_sum
    
    def minPath(self, row, col):
        
        if row == len(self.matrix):
            return 0
        
        if col == len(self.matrix[0]) or col < 0:
            return float('inf')
        
        if (row, col) not in self.memo:
            self.memo[(row, col)] = self.matrix[row][col] + \
            min(self.minPath(row+1, col-1), self.minPath(row+1, col), self.minPath(row+1, col+1))
            
        return self.memo[(row, col)]