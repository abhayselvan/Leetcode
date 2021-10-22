class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        if rowIndex == 0: 
            return [1]
        
        result = [1,1]
        
        for i in range(1,rowIndex):
            sol = [1]
            for j in range(1,len(result)):
                sol.append(result[j]+result[j-1])
            sol.append(1)
            result = sol
            
        return result