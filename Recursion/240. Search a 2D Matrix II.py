class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        self.matrix = matrix
        self.target = target
        
        return self._searchMatrix(0, len(matrix[0])-1)
        
    def _searchMatrix(self, x, y):
        
        if x > len(self.matrix) - 1 or y < 0:
            return False
        
        if self.matrix[x][y] == self.target:
            return True
        
        elif self.matrix[x][y] > self.target:
            return self._searchMatrix(x, y-1)
        
        else:
            return self._searchMatrix(x+1, y)
        