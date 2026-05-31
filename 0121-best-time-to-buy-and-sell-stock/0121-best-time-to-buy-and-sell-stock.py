class Solution:
    def maxProfit(self,prices):
        buy=prices[0]
        profit=0
        for p in prices:
            buy=min(buy,p)
            profit=max(profit,p-buy)
        return profit