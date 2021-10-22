class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        low = prices[0]
        profit = max_profit = 0
        
        for i in range(1, len(prices)):
            
            if prices[i] <= low:
                low = prices[i]
                
            else:
                profit = prices[i] - low
                max_profit = max(profit, max_profit)
                
        return max_profit
                
            