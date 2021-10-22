class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero_indices = []
        n = len(matrix)
        m = len(matrix[0])
        
        for i in range(n):
            for j in range(m):
                
                if matrix[i][j] == 0:
                    zero_indices.append((i,j))
                    
        for x, y in zero_indices:
            
            for i in range(n):
                matrix[i][y] = 0
                
            for j in range(m):
                matrix[x][j] = 0
                
        return matrix