class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        sell, buy = 0, 10e10
        n = len(prices)

        for i in range(n):
            buy = min(buy, prices[i])
            profit = max(profit, prices[i] - buy)
        return profit