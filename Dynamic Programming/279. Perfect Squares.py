class Solution:
    def numSquares(self, n: int) -> int:
        
        squares = [x*x for x in range(1,int(n**0.5)+1)]
        
        dp = [float('inf')] *(n+1)
        dp[0] = 0
        
        for i in range(len(dp)):
            
            for square in squares:
                
                if i < square:
                    break
                
                dp[i] = min(dp[i], dp[i-square] + 1)
                
        return dp[-1]
            