class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        profit = 0
        n = len(prices)

        if n==1:
            return 0
        buy, sell = prices[0], prices[0]

        for i in range(1,n):
            
            if prices[i] > buy:
                profit += (prices[i] - buy)
                buy = prices[i]
            buy = min(buy, prices[i])
            
        return profit

