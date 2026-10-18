from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n < 2:
            return 0    
        k = 0 
        max_profit = 0 
        
        for i in range(1, n):
            profit = prices[i] - prices[k]
        
            if profit > max_profit:
                max_profit = profit
            
            if prices[i] < prices[k]:
                k = i
                
        return max_profit
