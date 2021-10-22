class Solution:
    def totalNQueens(self, n: int) -> int:
        
        def backtrack(row, colset, diagonalset, antidiagonalset):
            
            if row == n:
                return 1
            
            solutions = 0
            
            for col in range(n):
                
                if col in colset or row-col in diagonalset or row+col in antidiagonalset:
                    continue
                    
                colset.add(col)
                diagonalset.add(row-col)
                antidiagonalset.add(row+col)
                
                solutions += backtrack(row+1, colset, diagonalset, antidiagonalset)
                
                colset.remove(col)
                diagonalset.remove(row-col)
                antidiagonalset.remove(row+col)
                
            return solutions
                
        return backtrack(0, set(), set(), set())