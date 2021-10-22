class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        result = []
        
        def backtrack(row, colset, diagonalset, antidiagonalset, path):
            
            if row == n:
                result.append(path)
                return
            
            for col in range(n):
                
                if col in colset or row-col in diagonalset or row+col in antidiagonalset:
                    continue
                    
                colset.add(col)
                diagonalset.add(row-col)
                antidiagonalset.add(row+col)
                
                rowString = ['.' for _ in range(n)]        
                rowString[col] = 'Q'
                
                backtrack(row+1, colset, diagonalset, antidiagonalset, path + ["".join(rowString)])
                
                colset.remove(col)
                diagonalset.remove(row-col)
                antidiagonalset.remove(row+col)
                
        backtrack(0, set(), set(), set(), [])
        
        return result