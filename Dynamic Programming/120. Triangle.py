class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        self.memo = {}
        self.triangle = triangle
        self.size = len(self.triangle)
        
        return self.minPath(0, 0)
        
    def minPath(self, row, col):
        
        if row == self.size:
            return 0
        
        if (row, col) not in self.memo:
        
            self.memo[(row, col)] = self.triangle[row][col] + min(self.minPath(row+1, col), self.minPath(row+1, col+1))
            
        return self.memo[(row, col)]