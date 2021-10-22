class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        MAX = float('inf')
        dp = [MAX]*(amount+1)
        dp[0] = 0
        
        
        for coin in coins:
            for i in range(coin,amount+1):
                
                dp[i] = min(dp[i],dp[i-coin]+1)
            
       
        return dp[amount] if dp[amount] != MAX else -1