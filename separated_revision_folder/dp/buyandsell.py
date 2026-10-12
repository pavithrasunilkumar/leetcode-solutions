class Solution:
    def maxProfit(self, prices):
        min_price = prices[0]
        max_profit = 0
        n=len(prices)
        for i in range(0,n):
            min_price=min(min_price,prices[i])
            max_profit=max(max_profit,prices[i]-min_price)
        return max_profit